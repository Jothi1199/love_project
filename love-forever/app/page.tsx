"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"

export default function Home() {
  const [password, setPassword] = useState("")
  const router = useRouter()

  const correctPassword = "Ammu1299"

  const handleUnlock = () => {
    if (password === correctPassword) {
      router.push("/love")
    } else {
      alert("Wrong password ❤️ Try again")
    }
  }

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-r from-pink-300 to-purple-300">
      <div className="bg-white p-10 rounded-3xl shadow-2xl text-center">
        <h1 className="text-3xl font-bold mb-6 text-pink-600">
          🔐 Enter Our Love Password
        </h1>

        <input
          type="password"
          placeholder="Enter password..."
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="border p-3 rounded-xl w-64"
        />

        <br />

        <button
          onClick={handleUnlock}
          className="mt-5 bg-pink-500 hover:bg-pink-600 text-white px-6 py-2 rounded-xl"
        >
          Unlock ❤️
        </button>
      </div>
    </div>
  )
}
