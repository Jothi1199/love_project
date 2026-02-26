"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Letter() {
  const [open, setOpen] = useState(false);
  const router = useRouter();

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-rose-50 text-center p-6">

      {!open ? (
        <div
          onClick={() => setOpen(true)}
          className="text-6xl cursor-pointer animate-pulse"
        >
          ❤️
        </div>
      ) : (
        <div className="max-w-xl">
          <h1 className="text-3xl mb-4">My Love Letter</h1>

          <p className="mb-4">
            (Write your emotional content here ❤️)
          </p>

          <p
            onClick={() => router.push("/love")}
            className="text-pink-600 cursor-pointer underline mt-6"
          >
            Can we go back to our memories by clicking this line...
          </p>
        </div>
      )}
    </div>
  );
}
