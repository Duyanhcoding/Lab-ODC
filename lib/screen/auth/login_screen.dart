import 'package:flutter/material.dart';

// Import đủ 4 màn hình chức năng (Đảm bảo đường dẫn đúng với dự án của bạn)
import '../enterprise/enterprise_home.dart';
import '../talent/talent_home.dart';
import '../mentor/mentor_home.dart';
import '../admin/admin_home.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  bool _isLoading = false;

  // --- HÀM XỬ LÝ CHÍNH: Hiện menu chọn vai trò ---
  void _handleLogin() async {
    // 1. Kiểm tra nhập liệu cho có lệ (giống thật)
    if (_emailController.text.isEmpty || _passwordController.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Vui lòng nhập tài khoản và mật khẩu"), backgroundColor: Colors.orange),
      );
      return;
    }

    // 2. Giả vờ Loading 1 chút
    setState(() => _isLoading = true);
    await Future.delayed(const Duration(milliseconds: 500)); 
    setState(() => _isLoading = false);

    // 3. HIỆN BẢNG CHỌN (POPUP MENU)
    if (mounted) {
      showDialog(
        context: context,
        barrierDismissible: false, // Bắt buộc phải chọn, không bấm ra ngoài được
        builder: (context) {
          return AlertDialog(
            title: const Text("Chọn vai trò trải nghiệm", textAlign: TextAlign.center, style: TextStyle(fontWeight: FontWeight.bold)),
            content: Column(
              mainAxisSize: MainAxisSize.min, // Thu gọn bảng vừa đủ nội dung
              children: [
                const Text("Bạn muốn đăng nhập dưới quyền gì?", style: TextStyle(fontSize: 13, color: Colors.grey)),
                const SizedBox(height: 20),
                
                // Nút 1: Ứng viên
                _buildRoleButton(
                  label: "Ứng viên (Talent)", 
                  icon: Icons.person, 
                  color: Colors.green,
                  roleKey: 'talent'
                ),
                
                // Nút 2: Doanh nghiệp
                _buildRoleButton(
                  label: "Doanh nghiệp", 
                  icon: Icons.business, 
                  color: Colors.blue,
                  roleKey: 'enterprise'
                ),

                // Nút 3: Mentor
                _buildRoleButton(
                  label: "Mentor / Giảng viên", 
                  icon: Icons.school, 
                  color: Colors.orange,
                  roleKey: 'mentor'
                ),

                // Nút 4: Admin
                _buildRoleButton(
                  label: "Quản trị viên (Admin)", 
                  icon: Icons.admin_panel_settings, 
                  color: Colors.red,
                  roleKey: 'admin'
                ),
              ],
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context), // Nút Hủy
                child: const Text("Hủy bỏ", style: TextStyle(color: Colors.grey)),
              )
            ],
          );
        },
      );
    }
  }

  // Hàm chuyển màn hình khi bấm nút
  void _navigateToRole(String role) {
    Navigator.pop(context); // Đóng bảng chọn lại trước

    // Tạo dữ liệu giả tương ứng với vai trò đã chọn
    final fakeUserData = {
      'user': {
        'id': 101,
        'email': _emailController.text,
        'full_name': 'Demo User ($role)',
        'role': role
      },
      'access_token': 'demo_token_123'
    };

    Widget nextScreen;
    // Phân luồng màn hình
    if (role == 'enterprise') {
      nextScreen = EnterpriseHomeScreen(userData: fakeUserData);
    } else if (role == 'mentor') {
      nextScreen = MentorHomeScreen(userData: fakeUserData);
    } else if (role == 'admin') {
      nextScreen = AdminHomeScreen(userData: fakeUserData);
    } else {
      nextScreen = TalentHomeScreen(userData: fakeUserData);
    }

    // Chuyển trang
    Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => nextScreen));
  }

  // Widget vẽ nút bấm cho đẹp
  Widget _buildRoleButton({required String label, required IconData icon, required Color color, required String roleKey}) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      width: double.infinity,
      child: ElevatedButton.icon(
        onPressed: () => _navigateToRole(roleKey),
        icon: Icon(icon, color: Colors.white),
        label: Text(label),
        style: ElevatedButton.styleFrom(
          backgroundColor: color,
          foregroundColor: Colors.white,
          padding: const EdgeInsets.symmetric(vertical: 12),
          alignment: Alignment.centerLeft, // Canh lề trái cho thẳng hàng
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Logo & Tiêu đề
              const Icon(Icons.account_tree_rounded, size: 80, color: Colors.blue),
              const SizedBox(height: 10),
              const Text("LAB ODC SYSTEM", style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold, color: Colors.blue)),
              const Text("Cổng đăng nhập Demo", style: TextStyle(color: Colors.grey)),
              const SizedBox(height: 40),

              // Form nhập liệu (Giữ nguyên để trông chuyên nghiệp)
              TextField(
                controller: _emailController,
                decoration: InputDecoration(
                  labelText: "Email",
                  prefixIcon: const Icon(Icons.email_outlined),
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  filled: true, fillColor: Colors.grey[50]
                ),
              ),
              const SizedBox(height: 15),
              TextField(
                controller: _passwordController,
                obscureText: true,
                decoration: InputDecoration(
                  labelText: "Mật khẩu",
                  prefixIcon: const Icon(Icons.lock_outline),
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  filled: true, fillColor: Colors.grey[50]
                ),
              ),
              
              const SizedBox(height: 25),

              // Nút Login chính
              SizedBox(
                width: double.infinity,
                height: 55,
                child: ElevatedButton(
                  onPressed: _isLoading ? null : _handleLogin,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.blue[800],
                    foregroundColor: Colors.white,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    elevation: 5,
                  ),
                  child: _isLoading 
                    ? const CircularProgressIndicator(color: Colors.white) 
                    : const Text("ĐĂNG NHẬP", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}