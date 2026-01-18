import 'package:flutter/material.dart';
import '../auth/login_screen.dart';

class TalentHomeScreen extends StatelessWidget {
  final Map<String, dynamic> userData;
  const TalentHomeScreen({super.key, required this.userData});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Text("Cổng Việc Làm (Talent)"),
        backgroundColor: Colors.green[700],
        foregroundColor: Colors.white,
        actions: [IconButton(onPressed: () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const LoginScreen())), icon: const Icon(Icons.logout))],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Banner
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              gradient: LinearGradient(colors: [Colors.green.shade400, Colors.green.shade800]),
              borderRadius: BorderRadius.circular(15),
            ),
            child: Row(
              children: [
                const Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Tìm công việc mơ ước!", style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
                      SizedBox(height: 5),
                      Text("Hơn 500+ dự án đang chờ bạn.", style: TextStyle(color: Colors.white70)),
                    ],
                  ),
                ),
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(10)),
                  child: const Icon(Icons.search, color: Colors.white, size: 30),
                )
              ],
            ),
          ),
          const SizedBox(height: 25),
          
          const Text("Việc làm gợi ý cho bạn", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          const SizedBox(height: 10),

          // Job List
          _buildJobCard("Frontend Developer (ReactJS)", "FPT Software", "15tr - 25tr", ["Remote", "Full-time"]),
          _buildJobCard("Thực tập sinh Python/AI", "Viettel AI", "Thỏa thuận", ["Hà Nội", "Part-time"]),
          _buildJobCard("UI/UX Designer", "VNG Corporation", "20tr - 30tr", ["HCM", "Hybrid"]),
          _buildJobCard("Flutter Mobile Dev", "Lab ODC", "10tr - 15tr", ["Đà Nẵng", "Full-time"]),
        ],
      ),
    );
  }

  Widget _buildJobCard(String title, String company, String salary, List<String> tags) {
    return Card(
      elevation: 2,
      margin: const EdgeInsets.only(bottom: 15),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                    Text(company, style: const TextStyle(color: Colors.grey)),
                  ],
                ),
                Icon(Icons.bookmark_border, color: Colors.green[700]),
              ],
            ),
            const SizedBox(height: 15),
            Row(
              children: tags.map((tag) => Container(
                margin: const EdgeInsets.only(right: 8),
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(color: Colors.grey[100], borderRadius: BorderRadius.circular(20)),
                child: Text(tag, style: TextStyle(fontSize: 12, color: Colors.grey[800])),
              )).toList(),
            ),
            const SizedBox(height: 15),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(salary, style: TextStyle(fontWeight: FontWeight.bold, color: Colors.green[800])),
                ElevatedButton(
                  onPressed: () {},
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.green[700],
                    foregroundColor: Colors.white,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20))
                  ),
                  child: const Text("Ứng tuyển"),
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}