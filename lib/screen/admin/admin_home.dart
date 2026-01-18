import 'package:flutter/material.dart';
import '../auth/login_screen.dart';

class AdminHomeScreen extends StatelessWidget {
  final Map<String, dynamic> userData;
  const AdminHomeScreen({super.key, required this.userData});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: const Text("ADMINISTRATOR"),
        backgroundColor: Colors.red[800],
        foregroundColor: Colors.white,
        centerTitle: true,
        actions: [IconButton(onPressed: () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const LoginScreen())), icon: const Icon(Icons.logout))],
      ),
      body: GridView.count(
        crossAxisCount: 2,
        padding: const EdgeInsets.all(16),
        crossAxisSpacing: 16,
        mainAxisSpacing: 16,
        children: [
          _buildAdminCard(Icons.people, "Người dùng", "1,205", Colors.blue),
          _buildAdminCard(Icons.business, "Doanh nghiệp", "340", Colors.orange),
          _buildAdminCard(Icons.work, "Dự án", "56", Colors.green),
          _buildAdminCard(Icons.report, "Báo cáo", "12", Colors.red),
          _buildAdminCard(Icons.settings, "Cài đặt", "System", Colors.grey),
          _buildAdminCard(Icons.notifications, "Thông báo", "New", Colors.amber),
        ],
      ),
    );
  }

  Widget _buildAdminCard(IconData icon, String title, String value, Color color) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 4, offset: const Offset(2, 2))],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 40, color: color),
          const SizedBox(height: 10),
          Text(value, style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: color)),
          Text(title, style: const TextStyle(color: Colors.grey)),
        ],
      ),
    );
  }
}