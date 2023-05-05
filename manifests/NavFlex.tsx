import React, { forwardRef } from "react";
import { motion } from "framer-motion";

export const NavFlex = forwardRef<
  HTMLDivElement,
  {
    styles: React.CSSProperties;
    children: React.ReactNode[];
    custom: {
        x?: number,
        duration?: number,
        hoverColor?: string
    };
    className?: string;
  }
>((props, ref) => {

    const variants={
        initial:{

        },
        animate:{

        },
        whileHover:{
            color: props.custom.hoverColor,
            x: props.custom.x,
            transition:{
                duration: props.custom.duration,
            }
        }
    }
  
  return (
    <motion.div
      ref={ref}
      style={{ ...props.styles, display: "flex", position: "relative" }}
      className={props.className}
      variants={variants}
      initial="initial"
      animate="animate"
      whileHover="whileHover"
    >
      {props.children}
    </motion.div>
  );
});

export default NavFlex;