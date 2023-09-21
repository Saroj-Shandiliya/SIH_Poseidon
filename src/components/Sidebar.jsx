import React, { useState } from 'react';
import {FaRegChartBar, FaMapMarkedAlt}from "react-icons/fa";
import {BiWater} from "react-icons/bi"
import {RiAccountPinCircleLine, RiArticleLine} from "react-icons/ri";
import {AiOutlineHome} from "react-icons/ai";
import { NavLink } from 'react-router-dom';
import logo from '../images/Indra_white1.png';

const Sidebar = ({children}) => {
    const[isOpen ,setIsOpen] = useState(false);
    const toggle = () => setIsOpen (!isOpen);
    const closing_toggle = () => setIsOpen (false);
    const menuItem=[
        {
            path:"/dashboard",
            name:"Dashboard",
            icon:<RiAccountPinCircleLine/>
        },
        {
            path:"/map-view",
            name:"MapView",
            icon:<FaMapMarkedAlt/>
        },
        {
            path:"/about",
            name:"About",
            icon:<RiArticleLine/>
        },
    ]
    return (
        <div className="container">
           <div style={{width: isOpen ? "300px" : "65px", borderRadius: isOpen ? "0px" : "100px", margin: isOpen ? "0px" : "0px 3px"}} className="sidebar">
               <div className="top_section">
                   <img style={{display: isOpen ? "block" : "none", position: "absolute", width: "270px", left:"-1rem", top:"-5.5rem"}} onClick={toggle} className="logo" src={logo} alt="Logo" />
                   <div style={{display: isOpen ? "none" : "block", marginLeft: isOpen ? "50px" : "0px"}} className="bars">
                       <BiWater onClick={toggle}/>
                   </div>
               </div>
               {
                   menuItem.map((item, index)=>(
                       <NavLink to={item.path} key={index} className="link" activeclassName="active " onClick={closing_toggle}>
                           <div className="icon" >{item.icon}</div>
                           <div style={{display: isOpen ? "block" : "none"}} className="link_text">{item.name}</div>
                       </NavLink>
                   ))
               }
           </div>
           <main>{children}</main>
        </div>
    );
};

export default Sidebar;