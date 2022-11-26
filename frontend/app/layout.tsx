import React from "react"
import Navbar from "../components/Navbar/Navbar"
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <head />
      <body>
        <Navbar />
        <div className="max-w-6xl mx-auto px-4 mt-4">
          {children}
        </div>
      </body>
    </html>
  )
}
