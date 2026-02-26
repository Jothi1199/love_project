"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

export default function Letter() {
  const [open, setOpen] = useState(false);
  const router = useRouter();

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-rose-100">

      {/* Page Title - Always Visible */}
      <h1 className="text-4xl font-serif font-bold text-pink-600 mb-10">
         Love Letter
      </h1>


      {!open ? (
        <div
          className="relative cursor-pointer [perspective:1000px]"
          onClick={() => setOpen(true)}
        >

          {/* Envelope Body */}
          <div className="w-80 h-52 bg-white shadow-xl relative z-10 rounded-md"></div>

          {/* Flap */}
          <div
            className="absolute top-0 w-80 h-40 bg-pink-300 origin-top transition-transform duration-1000"
            style={{
              transform: open ? "rotateX(180deg)" : "rotateX(0deg)",
              transformStyle: "preserve-3d",
            }}
          />

          {/* Heart */}
          <div className="absolute inset-0 flex items-center justify-center z-20 text-3xl">
            ❤️
          </div>

        </div>
      ) : (
        <TypewriterLetter />
      )}

    </div>
  );
}


/* ================= Letter Component ================= */

function TypewriterLetter() {
  const router = useRouter();
  const mainText = `My Love,

From the first moment to now,
every memory with you is my treasure.

You are my happiness,
my peace,
my forever. ❤️
`;

  const linkText =
    "Can we go back to our memories❤️...";

  const [main, setMain] = useState("");
  const [link, setLink] = useState("");
  const [mainDone, setMainDone] = useState(false);


  // Type main letter
  useEffect(() => {
    let i = 0;

    const mainTimer = setInterval(() => {

      setMain(mainText.slice(0, i));
      i++;

      if (i > mainText.length) {
        clearInterval(mainTimer);
        setMainDone(true);
      }

    }, 40);

    return () => clearInterval(mainTimer);

  }, []);


  // Type link after main is done
  useEffect(() => {

    if (!mainDone) return;

    let j = 0;

    const linkTimer = setInterval(() => {

      setLink(linkText.slice(0, j));
      j++;

      if (j > linkText.length) {
        clearInterval(linkTimer);
      }

    }, 40);

    return () => clearInterval(linkTimer);

  }, [mainDone]);


  return (
    <div className="max-w-xl bg-white p-8 shadow-2xl rounded-xl text-center">

      {/* Main Letter */}
      <pre className="whitespace-pre-wrap font-serif text-lg text-purple-700">

        {main}
      </pre>

      {/* Typed Link */}
      {mainDone && (
        <p
          onClick={() => router.push("/love")}
          className="text-pink-600 cursor-pointer underline mt-6"
        >
          {link}
        </p>
      )}

    </div>
  );
}
