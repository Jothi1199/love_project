"use client"

import { useState } from "react"

export default function LovePage() {
  const [videoEnded, setVideoEnded] = useState(false)

  if (!videoEnded) {
    return (
      <video
        src="/Cinematic_Love_Trailer.mp4"
        autoPlay
        muted
        onEnded={() => setVideoEnded(true)}
        className="w-full h-screen object-cover"
      />
    )
  }

  return (
    <div className="min-h-screen bg-black text-white text-center p-10">

      <audio autoPlay loop>
        <source src="/music.mpeg" type="audio/mpeg" />
      </audio>

      <h1 className="text-5xl font-bold mb-8 text-pink-500">
        Our Eternal Love ❤️
      </h1>

      <div className="flex justify-center gap-10 flex-wrap">
        <img src="/husband.jpeg" className="rounded-3xl w-64 shadow-2xl" />
        <img src="/son.jpeg" className="rounded-3xl w-64 shadow-2xl" />
      </div>

      <p className="mt-10 text-lg max-w-2xl mx-auto leading-relaxed">
        From our reception on 16.11.2024,
        to our marriage on 17.11.2024,
        to welcoming our little prince on 23.10.2025 —
        my life became complete.
        <br /><br />
        This love is forever.
      </p>
    </div>
  )
}
