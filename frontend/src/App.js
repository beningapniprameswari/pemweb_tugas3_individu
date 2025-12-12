import { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const analyzeReview = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/analyze-review", {
        text: text,
      });
      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Gagal menghubungi backend!");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px" }}>
      <h1>Product Review Analyzer</h1>

      <textarea
        rows={5}
        style={{ width: "100%" }}
        placeholder="Masukkan review produk..."
        onChange={(e) => setText(e.target.value)}
      ></textarea>

      <button onClick={analyzeReview} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Review"}
      </button>

      {result && (
        <div style={{ marginTop: "20px", padding: "10px", border: "1px solid #ccc" }}>
          <h3>Hasil:</h3>
          <p><b>Sentiment:</b> {result.sentiment}</p>
          <p><b>Keypoints:</b><br /> {result.keypoints}</p>
        </div>
      )}
    </div>
  );
}

export default App;
