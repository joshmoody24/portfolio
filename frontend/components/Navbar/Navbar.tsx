import NavbarLink from "./NavbarLink"

export default function Navbar() {
    return (
        <nav className="
            flex items-center justify-between
            w-full
            py-0
            px-4
            text-lg text-gray-700
            bg-white
            shadow-lg
            "
        >
            <div className="max-w-6xl mx-auto flex w-full items-center justify-between">
                {/* Website Logo */}
                <div className="mr-auto">
                    <a href="#" className="flex items-center py-4 px-2">
                        <img src="favicon.ico" alt="Logo" className="h-8 w-8 mr-2" />
                    </a>
                </div>
                {/* primary navbar menu */}
                <div className="flex ml-auto">
                    <NavbarLink to="/">Home</NavbarLink>
                    <NavbarLink to="/about">About</NavbarLink>
                    <NavbarLink to="/contact">Contact</NavbarLink>
                </div>
            </div>
        </nav>
    )
}