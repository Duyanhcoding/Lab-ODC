import 'package:flutter/material.dart';
import '../services/api_service.dart';  // Gọi API
import '../models/project.dart';        // Gọi Model Project
import 'auth/login_screen.dart';        // Gọi màn hình Login (đã chuyển vào thư mục auth)

class DashboardScreen extends StatefulWidget {
  final Map<String, dynamic> userData; // Thông tin user từ màn hình Login truyền sang

  const DashboardScreen({super.key, required this.userData});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  final ApiService _apiService = ApiService();
  late Future<List<dynamic>> _projectsFuture;

  @override
  void initState() {
    super.initState();
    // Gọi API lấy danh sách dự án ngay khi mở màn hình
    _projectsFuture = _apiService.getProjects();
  }

  // Hàm đăng xuất
  void _logout() {
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(builder: (context) => const LoginScreen()),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100], // Màu nền nhẹ
      appBar: AppBar(
        title: const Text("LabOdc Dashboard"),
        backgroundColor: Colors.blue,
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: _logout,
            tooltip: "Đăng xuất",
          )
        ],
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // --- Phần Header hiển thị tên User ---
          Container(
            padding: const EdgeInsets.all(20),
            color: Colors.white,
            width: double.infinity,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "Xin chào, ${widget.userData['name'] ?? 'Partner'}!",
                  style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 5),
                const Text("Dưới đây là các dự án đang hoạt động:", style: TextStyle(color: Colors.grey)),
              ],
            ),
          ),
          
          const SizedBox(height: 10),

          // --- Phần Danh Sách Dự Án (Lấy từ API) ---
          Expanded(
            child: FutureBuilder<List<dynamic>>(
              future: _projectsFuture,
              builder: (context, snapshot) {
                // 1. Đang tải (Hiện vòng xoay)
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const Center(child: CircularProgressIndicator());
                }

                // 2. Có lỗi
                if (snapshot.hasError) {
                  return Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Icon(Icons.error_outline, size: 40, color: Colors.red),
                        const SizedBox(height: 10),
                        Text("Lỗi kết nối: ${snapshot.error}"),
                        ElevatedButton(
                          onPressed: () {
                            setState(() {
                              _projectsFuture = _apiService.getProjects(); // Thử lại
                            });
                          }, 
                          child: const Text("Thử lại")
                        )
                      ],
                    ),
                  );
                }

                // 3. Không có dữ liệu
                if (!snapshot.hasData || snapshot.data!.isEmpty) {
                  return const Center(
                    child: Text("Chưa có dự án nào.", style: TextStyle(fontSize: 16, color: Colors.grey)),
                  );
                }

                // 4. Có dữ liệu -> Hiển thị list
                final projectsData = snapshot.data!;
                return ListView.builder(
                  padding: const EdgeInsets.all(10),
                  itemCount: projectsData.length,
                  itemBuilder: (context, index) {
                    // Map dữ liệu JSON sang Model
                    final project = Project.fromJson(projectsData[index]);
                    
                    return Card(
                      elevation: 2,
                      margin: const EdgeInsets.only(bottom: 12),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                      child: ListTile(
                        contentPadding: const EdgeInsets.all(16),
                        leading: CircleAvatar(
                          backgroundColor: Colors.blue.withOpacity(0.1),
                          child: const Icon(Icons.folder_open, color: Colors.blue),
                        ),
                        title: Text(
                          project.name, 
                          style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)
                        ),
                        subtitle: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const SizedBox(height: 5),
                            Text(project.description, maxLines: 2, overflow: TextOverflow.ellipsis),
                            const SizedBox(height: 8),
                            // Badge trạng thái
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                              decoration: BoxDecoration(
                                color: project.status == 'Active' ? Colors.green[50] : Colors.grey[200],
                                borderRadius: BorderRadius.circular(4),
                              ),
                              child: Text(
                                project.status,
                                style: TextStyle(
                                  fontSize: 12,
                                  color: project.status == 'Active' ? Colors.green : Colors.grey[700],
                                  fontWeight: FontWeight.bold
                                ),
                              ),
                            )
                          ],
                        ),
                        onTap: () {
                          print("Đã chọn dự án: ${project.id}");
                          // Sau này làm màn hình chi tiết dự án ở đây
                        },
                      ),
                    );
                  },
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}