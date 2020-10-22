$(document).ready(function () {
                $(".collapsible").collapsible();
                $(".datepicker").datepicker();
                $("select").formSelect();
                $(".sidenav").sidenav();
                $(".button-collapse").sidenav();
            });
            document.getElementById("matfix").addEventListener("click", function (e) {
                e.stopPropagation();
            });