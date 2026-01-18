import 'package:flutter/material.dart';
import '../auth/login_screen.dart';

class EnterpriseHomeScreen extends StatelessWidget {
  final Map<String, dynamic> userData; // Nhận dữ liệu user
  const EnterpriseHomeScreen({super.key, required this.userData});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: const Text("Dashboard Doanh Nghiệp"),
        backgroundColor: Colors.blue[900],
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const LoginScreen())),
          )
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header chào hỏi
            Text("Xin chào, ${userData['user']['name'] ?? 'Doanh nghiệp'}", 
                style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.blueGrey)),
            const SizedBox(height: 5),
            const Text("Hôm nay bạn có 3 ứng viên mới cần duyệt.", style: TextStyle(color: Colors.grey)),
            const SizedBox(height: 20),

            // Thống kê nhanh (Cards)
            Row(
              children: [
                _buildStatCard("Dự án Active", "12", Colors.orange, Icons.folder_open),
                const SizedBox(width: 12),
                _buildStatCard("Ứng viên", "45", Colors.green, Icons.people),
                const SizedBox(width: 12),
                _buildStatCard("Ngân sách", "\$5k", Colors.red, Icons.attach_money),
              ],
            ),
            const SizedBox(height: 25),

            // Danh sách Dự án
            const Text("Dự án đang chạy", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 10),

            _buildProjectItem("Xây dựng Website E-commerce", "Đang tuyển dụng", 0.3, Colors.blue),
            _buildProjectItem("App Mobile Booking (Flutter)", "Đang thực hiện", 0.7, Colors.purple),
            _buildProjectItem("Hệ thống AI Chatbot", "Hoàn thành", 1.0, Colors.green),
            _buildProjectItem("Nền tảng Blockchain", "Chờ duyệt", 0.0, Colors.grey),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {},
        label: const Text("Đăng Dự Án Mới"),
        icon: const Icon(Icons.add),
        backgroundColor: Colors.blue[900],
        foregroundColor: Colors.white,
      ),
    );
  }

  Widget _buildStatCard(String title, String count, Color color, IconData icon) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(15),
        decoration: BoxDecoration(color: color.withOpacity(0.1), borderRadius: BorderRadius.circular(12)),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Icon(icon, color: color, size: 28),
            const SizedBox(height: 10),
            Text(count, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: color)),
            Text(title, style: TextStyle(color: color.withOpacity(0.8), fontSize: 12)),
          ],
        ),
      ),
    );
  }

  Widget _buildProjectItem(String name, String status, double progress, Color color) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      child: ListTile(
        contentPadding: const EdgeInsets.all(12),
        leading: CircleAvatar(
          backgroundColor: color.withOpacity(0.1),
          child: Icon(Icons.layers, color: color),
        ),
        title: Text(name, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 5),
            Text(status, style: TextStyle(color: color, fontSize: 12)),
            const SizedBox(height: 8),
            LinearProgressIndicator(value: progress, backgroundColor: Colors.grey[200], color: color, minHeight: 6),
          ],
        ),
        trailing: const Icon(Icons.more_vert, color: Colors.grey),
      ),
    );
  }
}