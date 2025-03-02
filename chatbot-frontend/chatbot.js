import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { FaRobot, FaUser } from "react-icons/fa";
import "./Chatbot.css"; // Import CSS for styling

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input, timestamp: new Date().toLocaleTimeString() };
    setMessages((prev) => [...prev, userMessage]);

    setInput("");

    try {
      const response = await axios.post("http://localhost:5000/chat", { message: input });
      const botMessage = { sender: "bot", text: response.data.reply, timestamp: new Date().toLocaleTimeString() };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.sender}`}>
            <div className="chat-avatar">{msg.sender === "user" ? <FaUser /> : <FaRobot />}</div>
            <div className="chat-text">
              <p>{msg.text}</p>
              <span className="chat-time">{msg.timestamp}</span>
            </div>
          </div>
        ))}
        <div ref={chatEndRef}></div>
      </div>

      <div className="chat-input">
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type a message..." />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;


