"use client"

import { useEffect, useState } from "react"
import { motion } from "framer-motion"

export default function LovePage() {
  const [showMain, setShowMain] = useState(false)
  const [daysMarried, setDaysMarried] = useState(0)
  const [countdowns, setCountdowns] = useState({
    husband: 0,
    son: 0,
    you: 0,
  })

  useEffect(() => {
    const timer = setTimeout(() => setShowMain(true), 3000)

    const today = new Date()
    const marriage = new Date("2024-11-17")
    const diffDays = Math.floor(
      (today.getTime() - marriage.getTime()) / (1000 * 60 * 60 * 24)
    )
    setDaysMarried(diffDays)

    const nextDate = (month: number, day: number) => {
      let year = today.getFullYear()
      let date = new Date(year, month - 1, day)
      if (date < today) date = new Date(year + 1, month - 1, day)
      return Math.floor((date.getTime() - today.getTime()) / (1000 * 60 * 60 * 24))
    }

    setCountdowns({
      husband: nextDate(12, 2),
      you: nextDate(1, 1),
      son: nextDate(10, 23),
    })

    return () => clearTimeout(timer)
  }, [])

  if (!showMain) {
    return (
      <div className="flex items-center justify-center h-screen bg-black text-white text-4xl">
        ❤️ Our Love Story Begins ❤️
      </div>
    )
  }

  return (
    <div className="relative min-h-screen bg-gradient-to-r from-pink-200 via-purple-200 to-pink-200 text-center p-10 overflow-hidden">

      {/* Floating Hearts */}
      {[...Array(20)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute text-pink-500 text-2xl"
          initial={{ y: "100vh", x: Math.random() * 100 + "vw" }}
          animate={{ y: "-10vh" }}
          transition={{
            duration: 8 + Math.random() * 5,
            repeat: Infinity,
            delay: Math.random() * 5,
          }}
        >
          ❤️
        </motion.div>
      ))}

      <audio autoPlay loop>
        <source src="/music.mp3" type="audio/mpeg" />
      </audio>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 2 }}
      >
        <h1 className="text-4xl font-bold text-pink-700 mb-6">
          My Forever Family 💕
        </h1>

        <p className="text-xl mb-4">
          💍 Married for {daysMarried} beautiful days
        </p>

        <div className="flex justify-center gap-8 mt-6 flex-wrap">
          <img src="/husband.jpg" className="rounded-3xl shadow-xl w-56" />
          <img src="/son.jpg" className="rounded-3xl shadow-xl w-56" />
        </div>

        <div className="mt-8 text-lg space-y-2">
          <p>🎂 Husband birthday in {countdowns.husband} days</p>
          <p>🎂 Your birthday in {countdowns.you} days</p>
          <p>👶 Son birthday in {countdowns.son} days</p>
        </div>

        <p className="mt-8 max-w-2xl mx-auto">
          You are my strength, my happiness, my world.
          Our journey from 16.11.2024 to forever is my greatest blessing.
          I love you endlessly ❤️
        </p>
      </motion.div>
    </div>
  )
}
