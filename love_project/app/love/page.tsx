"use client"
import { useEffect, useState } from "react"

export default function LovePage() {
  const [showMain, setShowMain] = useState(false)
  const [daysMarried, setDaysMarried] = useState(0)

  useEffect(() => {
    setTimeout(() => setShowMain(true), 5000)

    fetch("http://localhost:8000/counters")
      .then(res => res.json())
      .then(data => setDaysMarried(data.days_married))
  }, [])

  if (!showMain) {
    return (
      <div className="flex items-center justify-center h-screen bg-black text-white text-4xl animate-pulse">
        ❤️ Our Love Story Begins ❤️
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-r from-pink-200 to-purple-200 text-center p-10">
      <audio autoPlay loop>
        <source src="/music.mp3" type="audio/mpeg" />
      </audio>

      <h1 className="text-4xl font-bold mb-6">My Forever Family 💕</h1>
      <p className="text-xl mb-4">Married for {daysMarried} days 💍</p>

      <div className="flex justify-center gap-10 mt-10">
        <img src="/husband.jpg" className="rounded-2xl shadow-xl w-64" />
        <img src="/son.jpg" className="rounded-2xl shadow-xl w-64" />
      </div>

      <p className="mt-10 text-lg max-w-2xl mx-auto">
        My dear husband, you are my strength and my forever love.
        My sweet baby boy, you are my greatest blessing.
        I love you both beyond words ❤️
      </p>
    </div>
  )
}
