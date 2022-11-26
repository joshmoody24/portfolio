import Link from "next/link"

export default function NavbarLink({
    to,
    active,
    children,
}:{
    to: string,
    active?: boolean,
    children?: React.ReactNode
}){
    const baseClasses = "py-4 px-2 text-gray-500 font-semibold hover:text-green-500 transition duration-300"
    const activeClasses = "py-4 px-2 text-green-500 border-b-4 border-green-500 font-semibold"
    return <Link className={active ? activeClasses : baseClasses} href={to}>{children}</Link>
}