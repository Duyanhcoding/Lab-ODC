import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // 10.0.2.2 là địa chỉ localhost của máy tính khi nhìn từ máy ảo Android
  static const String baseUrl = 'http://10.0.2.2:8000/api'; 

  // --- HÀM LOGIN ---
  static Future<Map<String, dynamic>?> login(String email, String password) async {
    try {
      final url = Uri.parse('$baseUrl/login/'); // Gọi vào đường dẫn đăng nhập
      
      print("Đang gọi API: $url");
      print("Data gửi đi: $email / $password");

      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'email': email,
          'password': password,
        }),
      );

      print("Server trả về code: ${response.statusCode}");
      print("Nội dung server: ${response.body}");

      if (response.statusCode == 200) {
        // Đăng nhập thành công, trả về dữ liệu User
        return jsonDecode(response.body);
      } else {
        // Đăng nhập thất bại
        return null;
      }
    } catch (e) {
      print("Lỗi kết nối Server: $e");
      return null;
    }
  }
}