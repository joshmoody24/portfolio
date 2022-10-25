export default function Navbar() {
  return (
    <nav className="
        flex flex-wrap flex-row
        items-center
        justify-between
        w-full
        py-4
        md:py-0
        px-4
        text-lg text-gray-700
        bg-white
        shadow-lg
        "
    >
        <div className="max-w-6xl mx-auto px-4">
            <div className="flex justify-between">
                <div className="flex space-x-7">
                    {/* Website Logo */}
					<div>
						<a href="#" className="flex items-center py-4 px-2">
							<img src="favicon.ico" alt="Logo" className="h-8 w-8 mr-2" />
							<span className="font-semibold text-gray-500 text-lg">
                                Navigation
                            </span>
						</a>
					</div>
                    {/* primary navbar menuy */}
					<div className="hidden md:flex items-center space-x-1">
						<a
							href=""
							className="py-4 px-2 text-green-500 border-b-4 border-green-500 font-semibold"
                        >
                            Home
                        </a>
						<a
							href="/about"
							className="py-4 px-2 text-gray-500 font-semibold hover:text-green-500 transition duration-300"
                        >
							About
                        </a>
						<a
							href="/contact"
							className="py-4 px-2 text-gray-500 font-semibold hover:text-green-500 transition duration-300"
                        >
                            Contact
                        </a>
					</div>
                </div>
            </div>
        </div>
    </nav>
  )
}