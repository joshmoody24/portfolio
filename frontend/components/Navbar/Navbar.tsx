import NavbarLink from "./NavbarLink"

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
                            </a>
                        </div>
                        {/* primary navbar menu */}
                        <div className="hidden md:flex items-center space-x-1">
                            <NavbarLink to="/">Home</NavbarLink>
                            <NavbarLink to="/about">About</NavbarLink>
                            <NavbarLink to="/contact">Contact</NavbarLink>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    )
}