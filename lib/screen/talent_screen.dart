import 'package:flutter/material.dart';
import '../auth/login_screen.dart'; // Import để làm nút Đăng xuất hẳn (nếu cần)

class TalentHomeScreen extends StatelessWidget {
  final Map<String, dynamic> userData;
  const TalentHomeScreen({super.key, required this.userData});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Talent Dashboard"),
        backgroundColor: Colors.green,
        // Mặc định Flutter sẽ tự hiện nút Back (<) ở đây.
        // Khi bấm nút Back này -> Nó sẽ quay về RoleSelectionScreen.
        
        actions: [
          // Thêm nút Đăng Xuất (Logout) ở góc phải
          // Nút này dành cho trường hợp muốn thoát hẳn ra màn hình Đăng Nhập
          IconButton(
            icon: const Icon(Icons.logout, color: Colors.white),
            tooltip: "Đăng xuất về Login",
            onPressed: () {
               // Xóa sạch lịch sử để về thẳng Login
               Navigator.pushAndRemoveUntil(
                context,
                MaterialPageRoute(builder: (context) => const LoginScreen()),
                (route) => false,
              );
            },
          )
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.dashboard, size: 80, color: Colors.green),
            const SizedBox(height: 20),
            Text("Xin chào ${userData['user']['email']}"),
            const SizedBox(height: 10),
            const Text("Đây là giao diện Talent"),
            const SizedBox(height: 40),
            
            // Nút minh họa "Đổi Vai Trò"
            ElevatedButton.icon(
              icon: const Icon(Icons.swap_horiz),
              label: const Text("Chọn vai trò khác (Back)"),
              onPressed: () {
                // Lệnh pop này tương đương với nút Back trên điện thoại
                Navigator.pop(context); 
              },
            ),
          ],
        ),
      ),
    );
  }
}