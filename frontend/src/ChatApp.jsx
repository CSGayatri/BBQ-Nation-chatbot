import { useState } from "react";
import { Send } from "lucide-react";

export default function ChatFrontend() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;
    const userMessage = { role: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    try {
      // 1. Log the interaction to /log
      await fetch("http://127.0.0.1:8000/log", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          modality: "Call",
          call_time: new Date().toISOString(),
          phone_number: "9876543210",
          call_outcome: "AVAILABILITY",
          room_name: "Barbeque Nation Delhi",
          booking_date: "2025-05-21",
          booking_time: "18:30",
          number_of_guests: 4,
          call_summary: input,
        }),
      });

      // 2. Fetch reply from knowledge base
      const infoResponse = await fetch(
  `http://127.0.0.1:8000/api/get_info?query=${encodeURIComponent(input)}`
);

      const infoData = await infoResponse.json();

      let replyText = "Sorry, I couldn't find that information.";
      if (infoData.chunks && infoData.chunks.length > 0) {
        replyText = infoData.chunks[0];
      } else if (infoData.error) {
        replyText = infoData.error;
      }

      const botMessage = { role: "bot", text: replyText };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      const botMessage = {
        role: "bot",
        text: "Something went wrong. Please try again.",
      };
      setMessages((prev) => [...prev, botMessage]);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <div className="bg-green-600 text-white text-xl p-4 font-semibold">
        Barbeque Nation Assistant
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-2 flex flex-col">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`max-w-xs p-3 rounded-2xl shadow-md ${
              msg.role === "user"
                ? "bg-green-500 text-white self-end ml-auto"
                : "bg-white text-gray-900 self-start mr-auto"
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>

      <div className="border-t shadow-inner p-2 flex items-center space-x-2">
        <input
          type="text"
          className="flex-1 rounded-full border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-green-500"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
        />
        <button
          className="rounded-full bg-green-600 p-2 text-white hover:bg-green-700 transition"
          onClick={handleSend}
        >
          <Send className="h-5 w-5" />
        </button>
      </div>
    </div>
  );
}
