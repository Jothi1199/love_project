
"use client"
import { useState } from "react";

export default function Final() {
  const [showChoco, setShowChoco] = useState(false);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-pink-100">

      {!showChoco ? (
        <div
          onClick={() => setShowChoco(true)}
          className="flex flex-col items-center cursor-pointer animate-pulse"
        >


          {/* Big Heart */}
          <div className="text-[40vw] leading-none select-none">
            ❤️
          </div>

        </div>
      ) : (
        <img
          src="/dairy.jpeg"
          className="w-80 rounded-xl shadow-xl"
          alt="Chocolate"
        />
      )}

    </div>
  );
}
