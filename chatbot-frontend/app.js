// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import { motion } from "framer-motion";

// const Chatbot = () => {
//   const [messages, setMessages] = useState([
//     { text: "Hello! How can I help you today?", sender: "bot", timestamp: new Date() },
//   ]);
//   const [input, setInput] = useState("");

//   const sendMessage = async () => {
//     if (!input.trim()) return;

//     // Add user message to UI
//     const newMessage = { text: input, sender: "user", timestamp: new Date() };
//     setMessages([...messages, newMessage]);
//     setInput("");

//     try {
//       // Send message to backend
//       const response = await axios.post("http://localhost:5000/chat", { message: input });

//       // Add bot response to UI
//       setMessages((prev) => [...prev, { text: response.data.reply, sender: "bot", timestamp: new Date() }]);
//     } catch (error) {
//       console.error("Error communicating with bot:", error);
//     }
//   };

//   return (
//     <div style={{ maxWidth: "500px", margin: "auto", padding: "20px", border: "1px solid #ddd", borderRadius: "10px" }}>
//       <div style={{ height: "400px", overflowY: "auto", padding: "10px" }}>
//         {messages.map((msg, index) => (
//           <motion.div
//             key={index}
//             initial={{ opacity: 0, x: msg.sender === "bot" ? -50 : 50 }}
//             animate={{ opacity: 1, x: 0 }}
//             transition={{ duration: 0.3 }}
//             style={{
//               backgroundColor: msg.sender === "bot" ? "#e3f2fd" : "#dcedc8",
//               padding: "10px",
//               borderRadius: "10px",
//               margin: "5px 0",
//               alignSelf: msg.sender === "bot" ? "flex-start" : "flex-end",
//             }}
//           >
//             <strong>{msg.sender === "bot" ? "Bot" : "You"}:</strong> {msg.text}
//             <div style={{ fontSize: "10px", color: "#777", marginTop: "5px" }}>
//               {msg.timestamp.toLocaleTimeString()}
//             </div>
//           </motion.div>
//         ))}
//       </div>
//       <input
//         type="text"
//         value={input}
//         onChange={(e) => setInput(e.target.value)}
//         placeholder="Type a message..."
//         style={{ width: "80%", padding: "10px", borderRadius: "5px", border: "1px solid #ddd" }}
//       />
//       <button onClick={sendMessage} style={{ padding: "10px", marginLeft: "10px", borderRadius: "5px" }}>
//         Send
//       </button>
//     </div>
//   );
// };

// export default Chatbot;
import React from "react";
import Chatbot from "./components/Chatbot";

function App() {
  return (
    <div className="App">
      <h1>AI Chatbot</h1>
      <Chatbot />
    </div>
  );
}

export default App;

