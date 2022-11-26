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
        {children}
      </body>
    </html>
  )
}
