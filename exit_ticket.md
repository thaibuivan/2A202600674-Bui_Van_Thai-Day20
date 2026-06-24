# Exit Ticket: Multi-Agent Research System

**Câu 1: Case nào nên dùng multi-agent? Vì sao?**
Nên dùng Multi-agent cho các bài toán phức tạp, có quy trình nhiều bước hoặc đòi hỏi các kỹ năng chuyên môn khác biệt (ví dụ: thu thập dữ liệu, phân tích rủi ro, và tổng hợp báo cáo).
*Vì sao:* Vì thiết kế Multi-agent giúp tách biệt trách nhiệm (Separation of Concerns). Mỗi Agent sẽ được cấu hình một vai trò (Role) và câu lệnh (Prompt) tập trung vào một nhiệm vụ duy nhất, giúp tăng chất lượng đầu ra, dễ dàng gỡ lỗi (debug) từng bước và hạn chế tình trạng mô hình bị "ảo giác" (hallucination) khi phải xử lý quá nhiều thông tin cùng lúc.

**Câu 2: Case nào không nên dùng multi-agent? Vì sao?**
Không nên dùng Multi-agent cho các tác vụ đơn giản, mang tính chất một chiều (one-shot) như: dịch thuật, phân loại văn bản, tóm tắt một đoạn tin tức, hoặc giải quyết các truy vấn cơ bản.
*Vì sao:* Vì kiến trúc Multi-agent tốn rất nhiều thời gian phản hồi (Latency cao do phải trao đổi qua lại giữa các node) và làm tăng chi phí API đáng kể (do phải chạy qua nhiều mô hình). Với những bài toán đơn giản, một Single-agent (Baseline) là đủ để giải quyết nhanh chóng, tiết kiệm mà vẫn đảm bảo độ chính xác.
