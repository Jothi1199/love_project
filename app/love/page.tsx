
"use client"

import { useState } from "react"

import { useRouter } from "next/navigation";

export default function LovePage() {
  const [videoEnded, setVideoEnded] = useState(false)
  const [open, setOpen] = useState(false);
  const router = useRouter();

  if (!videoEnded) {
    return (
      <video
        src="/Cinematic_Love_Trailer_original.mp4"
        autoPlay
        onEnded={() => router.push("/final")}
        className="w-full h-screen object-cover"
      />
    )
  }

}
