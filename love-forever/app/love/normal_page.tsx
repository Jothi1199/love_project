"use client"

import { useEffect, useState } from "react"

export default function LovePage() {
  const [showMain, setShowMain] = useState(false)
  const [daysMarried, setDaysMarried] = useState(0)

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowMain(true)
    }, 3000)

    const marriageDate = new Date("2024-11-17")
    const today = new Date()
    const diffTime = today.getTime() - marriageDate.getTime()
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))
    setDaysMarried(diffDays)

    return () => clearTimeout(timer)
  }, [])

  if (!showMain) {
    return (
      <div className="flex items-center justify-center h-screen bg-black text-white text-3xl">
        ❤️ Our Love Story Begins ❤️
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-pink-100 text-center p-10">
      <h1 className="text-4xl font-bold text-pink-600 mb-6">
        My Forever Family 💕
      </h1>

      <p className="text-xl mb-6">
        💍 Married for {daysMarried} beautiful days
      </p>

      <p className="max-w-xl mx-auto text-lg">
        My dear husband, you are my strength and forever love.
        My sweet baby boy, you are my greatest blessing.
        I love you both endlessly ❤️
      </p>
    </div>
  )
}
