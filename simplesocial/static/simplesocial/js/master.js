
(function() {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    let canvasWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    let canvasHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

    const fireflies = [];
    const numberOfFirefly = 30;
    const birthToGive = 35;

    const colorPalettes = [
        ['#2F294F', 'rgba(74,49,89,', 'rgba(130,91,109,', 'rgba(185,136,131,', 'rgba(249,241,204,']
    ];

    const colorTheme = 0;
    const mainSpeed = 1;

    function setCanvasSize() {
        canvasWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        canvasHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
        canvas.setAttribute('width', canvasWidth);
        canvas.setAttribute('height', canvasHeight);
    }

    function getRandomInt(min, max, except) {
        let num;
        do {
            num = Math.floor(Math.random() * (max - min + 1)) + min;
        } while (except && ((Array.isArray(except) && num >= except[0] && num <= except[1]) || num === except));
        return num;
    }

    class Firefly {
            constructor(id, x = null, y = null) {
            this.id = id;
            this.width = getRandomInt(3, 6);
            this.height = getRandomInt(3, 6);
            this.x = x !== null ? x : getRandomInt(0, canvas.width - this.width);
            this.y = y !== null ? y : getRandomInt(0, canvas.height - this.height);
            this.speed = (this.width <= 10) ? 5 : 5;
            this.alpha = 1;
            this.alphaReduction = getRandomInt(1, 3) / 1000;
            this.color = colorPalettes[colorTheme][getRandomInt(0, colorPalettes[colorTheme].length - 1)];
            this.direction = getRandomInt(0, 360);
            this.turner = getRandomInt(0, 1) === 0 ? -1 : 1;
            this.turnerAmp = getRandomInt(1, 2);
            this.stepCounter = 0;
            this.changeDirectionFrequency = getRandomInt(1, 200);
            this.shadowBlur = getRandomInt(5, 25);
        }

        updatePosition() {
            let nextX = this.x + Math.cos(this.direction * Math.PI / 180) * this.speed;
            let nextY = this.y + Math.sin(this.direction * Math.PI / 180) * this.speed;

            if (nextX >= (canvas.width - this.width) || nextX <= 0) {
                this.direction = (nextX >= (canvas.width - this.width)) ? getRandomInt(90, 270) : getRandomInt(-90, 90);
                nextX = Math.max(0, Math.min(canvas.width - this.width, nextX));
            }

            if (nextY >= (canvas.height - this.height) || nextY <= 0) {
                this.direction = (nextY >= (canvas.height - this.height)) ? getRandomInt(180, 360) : getRandomInt(0, 180);
                nextY = Math.max(0, Math.min(canvas.height - this.height, nextY));
            }

            this.x = nextX;
            this.y = nextY;
            this.stepCounter++;

            if (this.changeDirectionFrequency && this.stepCounter >= this.changeDirectionFrequency) {
                this.turner *= -1;
                this.turnerAmp = getRandomInt(1, 2);
                this.stepCounter = 0;
                this.changeDirectionFrequency = getRandomInt(1, 200);
            }

            this.direction += this.turner * this.turnerAmp;
        }

        render() {
            context.beginPath();
            context.fillStyle = this.color + this.alpha + ")";
            context.arc(this.x + (this.width / 2), this.y + (this.height / 2), this.width / 2, 0, 2 * Math.PI);
            context.shadowColor = this.color + this.alpha + ")";
            context.shadowBlur = this.shadowBlur;
            context.fill();

            if (this.id > 15) {
                this.alpha -= this.alphaReduction;
                if (this.alpha <= 0) {
                    this.die();
                }
            }
        }

        die() {
            fireflies.splice(this.id, 1);
        }

        update() {
            this.updatePosition();
            this.render();
        }
    }

    function instantiatePopulation() {
        for (let i = 0; i < numberOfFirefly; i++) {
            fireflies.push(new Firefly(i));
        }
    }

    function animate() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        fireflies.forEach(firefly => firefly.update());
        requestAnimationFrame(animate);
    }

    canvas.onclick = function(e) {
        giveBirth(e, birthToGive);
    };

    function giveBirth(e, count) {
        for (let i = 0; i < count; i++) {
            const newFirefly = new Firefly(fireflies.length);
            newFirefly.x = e.offsetX;
            newFirefly.y = e.offsetY;
            fireflies.push(newFirefly);
        }
    }

    window.onload = function() {
        setCanvasSize();
        instantiatePopulation();
        animate();
    };

    window.onresize = setCanvasSize;
})();




// SOURCE: http://codepen.io/Thibka/pen/mWGxNj


