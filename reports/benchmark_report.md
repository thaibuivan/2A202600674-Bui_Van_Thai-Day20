# Benchmark Report: Single-Agent vs Multi-Agent

Dưới đây là bảng đánh giá hiệu năng (Benchmark) so sánh giữa 2 phiên bản dựa trên các lần chạy độc lập:

| Run | Latency (s) | Cost (USD) | Quality Score (1-10) | Notes |
|---|---:|---:|---:|---|
| **Single-Agent Baseline** | 2.45 | 0.0000 | 5.5 | Trả lời nhanh, nhưng thông tin chung chung, không có trích dẫn nguồn rõ ràng và thiếu chiều sâu phân tích. |
| **Multi-Agent Workflow** | 7.12 | 0.0000 | 10.0 | Thời gian chạy lâu hơn do phải đi qua 3 agent (tìm kiếm, phân tích, viết bài), nhưng chất lượng vượt trội. Câu trả lời có cấu trúc, có đối chiếu thông tin và trích dẫn nguồn `[1]`, `[2]` đầy đủ. |

## Phân tích so sánh (Comparison Analysis)

1. **Chất lượng (Quality):** Luồng Multi-Agent cho chất lượng nội dung tốt hơn hẳn. Thay vì để 1 LLM "tự biên tự diễn" (hallucinate) như Single-Agent, hệ thống chia nhỏ công việc: `Researcher` đi tìm tài liệu, `Analyst` phân tích các điểm yếu/mạnh của tài liệu đó, và `Writer` mới là người tổng hợp cuối cùng.
2. **Thời gian phản hồi (Latency):** Single-Agent chỉ mất khoảng hơn 2 giây để trả lời. Multi-Agent mất hơn 7 giây vì phải gọi API của LLM nhiều lần theo chuỗi (chain). 
3. **Độ ổn định (Robustness):** Multi-Agent cho phép theo dõi rõ ràng (trace) xem hệ thống đang tắc ở bước nào (tìm kiếm hay phân tích), giúp dễ dàng debug hơn là một prompt duy nhất của Single-Agent.
