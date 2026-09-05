// =================================
// PAGE LOADED
// =================================

document.addEventListener(
    "DOMContentLoaded",
    function () {


        // =================================
        // SCROLL REVEAL
        // =================================

        const revealElements =
            document.querySelectorAll(".reveal");


        const observer =
            new IntersectionObserver(
                function (entries) {

                    entries.forEach(
                        function (entry) {

                            if (
                                entry.isIntersecting
                            ) {

                                entry.target.classList.add(
                                    "visible"
                                );

                                observer.unobserve(
                                    entry.target
                                );

                            }

                        }
                    );

                },
                {
                    threshold: 0.12
                }
            );


        revealElements.forEach(
            function (element) {

                observer.observe(element);

            }
        );



        // =================================
        // CHARACTER COUNTER
        // =================================

        const messageInput =
            document.getElementById(
                "message"
            );


        const counter =
            document.getElementById(
                "counter"
            );


        if (
            messageInput &&
            counter
        ) {

            function updateCounter() {

                const length =
                    messageInput.value.length;


                counter.textContent =
                    `${length} / 500`;

            }


            messageInput.addEventListener(
                "input",
                updateCounter
            );


            updateCounter();

        }



        // =================================
        // FLASH MESSAGE AUTO HIDE
        // =================================

        const flashMessage =
            document.querySelector(
                ".flash-message"
            );


        if (flashMessage) {

            setTimeout(
                function () {

                    flashMessage.style.opacity =
                        "0";

                    flashMessage.style.transition =
                        "opacity 0.5s ease";


                    setTimeout(
                        function () {

                            flashMessage.remove();

                        },
                        500
                    );

                },
                4500
            );

        }



        // =================================
        // BUTTON CLICK EFFECT
        // =================================

        const buttons =
            document.querySelectorAll(
                ".primary-button"
            );


        buttons.forEach(
            function (button) {

                button.addEventListener(
                    "click",
                    function () {

                        button.style.transform =
                            "scale(0.97)";


                        setTimeout(
                            function () {

                                button.style.transform =
                                    "";

                            },
                            120
                        );

                    }
                );

            }
        );

    }
);