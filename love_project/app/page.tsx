"use client"
import { useState } from "react"
import { useRouter } from "next/navigation"

export default function Home() {
  const [password, setPassword] = useState("")
  const router = useRouter()

  const handleLogin = async () => {
    const res = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    })
    const data = await res.json()
    if (data.status === "success") {
      router.push("/love")
    } else {
      alert("Wrong password ❤️")
    }
  }

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-pink-100">
      <h1 className="text-3xl font-bold mb-6">Enter Our Love Password 💕</h1>
      <input
        type="password"
        className="p-3 rounded-xl"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button
        onClick={handleLogin}
        className="mt-4 bg-pink-500 text-white px-6 py-2 rounded-xl"
      >
        Unlock ❤️
      </button>
    </div>
  )
}
