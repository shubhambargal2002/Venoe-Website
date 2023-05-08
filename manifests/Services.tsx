import React, { useState, useEffect } from "react";
import { useAnimate, stagger, motion } from "framer-motion";

const staggerMenuItems = stagger(0.1, { startDelay: 0.15 });

function useMenuAnimation(isOpen: boolean) {
  const [scope, animate] = useAnimate();

  useEffect(() => {
    animate(".arrow", { rotate: isOpen ? 180 : 0 }, { duration: 0.2 });

    animate(
      "ul",
      {
        clipPath: isOpen
          ? "inset(0% 0% 0% 0% round 10px)"
          : "inset(10% 50% 90% 50% round 10px)"
      },
      {
        type: "spring",
        bounce: 0,
        duration: 0.5
      }
    );

    animate(
      "li",
      isOpen
        ? { opacity: 1, scale: 1, filter: "blur(0px)" }
        : { opacity: 0, scale: 0.3, filter: "blur(20px)" },
      {
        duration: 0.2,
        delay: isOpen ? staggerMenuItems : 0
      }
    );
  }, [isOpen]);

  return scope;
}

const Services = React.forwardRef<
	HTMLDivElement,
	{
        styles: React.CSSProperties;
		custom: {
		};
        className?: string;
	}
>((props, ref) => {

    const [isOpen, setIsOpen] = useState(false);
    const scope = useMenuAnimation(isOpen);

	return (
		<div ref={ref} className={props.className} style={props.styles}>
            <nav ref={scope} >
      <motion.button
        whileTap={{ scale: 0.97 }}
        onClick={() => setIsOpen(!isOpen)}
        style={{backgroundColor:"#ffffff", 
              display:"flex", 
              flexDirection:"row", 
              columnGap: "10px",
              alignItems:"center",
              fontFamily: "Space Grotesk", 
              fontWeight: 700, 
              fontSize: "16px",
              border:"none"
            }}
      >
        Services
        <div className="arrow" style={{ transformOrigin: "50% 55%" }}>
          <svg width="15" height="15" viewBox="0 0 20 20">
            <path d="M0 7 L 20 7 L 10 16" />
          </svg>
        </div>
      </motion.button>
      <ul
        style={{
          pointerEvents: isOpen ? "auto" : "none",
          clipPath: "inset(10% 50% 90% 50% round 10px)",
          display: "flex",
          flexDirection: "column",
          rowGap: "10px",
        }}
      >
        <li style={{listStyle: "none", margin:0}}>Service 1 </li>
        <li style={{listStyle: "none", margin:0}}>Service 2 </li>
        <li style={{listStyle: "none", margin:0}}>Service 3 </li>
        <li style={{listStyle: "none", margin:0}}>Service 4 </li>
      </ul>{" "}
    </nav>
		</div>
	);
});

export default Services;