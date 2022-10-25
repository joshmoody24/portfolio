import React, {FC, PropsWithChildren} from "react"
import Navbar from "./Navbar"

type Props = PropsWithChildren<{}>;

const Layout: FC<Props> = ({children}) => {
  return (
    <>
    <Navbar />
        <main>{children}</main>
    </>
  )
}

export default Layout;