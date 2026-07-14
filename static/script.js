document.addEventListener("DOMContentLoaded", function(){



    // ==========================
    // Smooth Scroll Navbar
    // ==========================


    const navLinks = document.querySelectorAll(
        ".navbar a"
    );


    navLinks.forEach(function(link){


        link.addEventListener(
            "click",
            function(event){


                const section =
                document.querySelector(
                    this.getAttribute("href")
                );


                if(section){


                    event.preventDefault();


                    section.scrollIntoView({

                        behavior:"smooth"

                    });


                }


            }
        );


    });







    // ==========================
    // Predict Button Loading
    // ==========================


    const form =
    document.querySelector(
        ".predict-form"
    );



    if(form){


        form.addEventListener(
            "submit",
            function(){


                const button =
                document.querySelector(
                    ".input-group button"
                );


                button.innerHTML =
                "🌱 Predicting...";


                button.disabled = true;


            }
        );


    }








    // ==========================
    // Input Validation
    // ==========================


    const inputs =
    document.querySelectorAll(
        ".input-group input"
    );



    inputs.forEach(function(input){



        input.addEventListener(
            "input",
            function(){


                if(this.value < 0){


                    alert(
                    "Please enter positive values only!"
                    );


                    this.value="";


                }


            }
        );



    });








    // ==========================
    // Crop Image Animation
    // ==========================


    const cropImage =
    document.querySelector(
        ".crop-image"
    );



    if(cropImage){


        cropImage.style.opacity="0";

        cropImage.style.transition=
        "opacity 1s ease";



        cropImage.onload=function(){


            cropImage.style.opacity="1";


        };


    }








    // ==========================
    // Auto Scroll To Result
    // ==========================


    const result =
    document.querySelector(
        ".result-section"
    );


    if(result){


        setTimeout(function(){


            result.scrollIntoView({

                behavior:"smooth"

            });


        },700);


    }

});