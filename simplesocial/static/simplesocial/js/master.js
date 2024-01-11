(function () {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    let canvasWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    let canvasHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

    let stars = [];
    const numberOfStars = 30;
    const birthToGive = 35;

    const colorPalettes = [
        'rgba(200, 0, 255, ',  // Light Purple
        'rgba(10, 16, 48, ', // Blue
        'rgba(120, 120, 120, ', // Grey
        'rgba(255, 105, 180, ', // Pink
        'rgba(255, 255, 255, ', // Bright White
        'rgba(106, 90, 205, ', // Dark Purple
    ];

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

    class Star {
        constructor(id, x = null, y = null) {
            this.id = id;
            this.width = getRandomInt(3, 6);
            this.height = getRandomInt(3, 6);
            this.x = x !== null ? x : getRandomInt(0, canvasWidth - this.width);
            this.y = y !== null ? y : getRandomInt(0, canvasHeight - this.height);
            this.speed = this.width <= 10 ? .7 : 1.2;
            this.alpha = 1;
            this.alphaReduction = getRandomInt(1, 3) / 1000;
            this.color = colorPalettes[getRandomInt(0, colorPalettes.length - 1)]; // Randomly select color
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

            if (nextX >= (canvasWidth - this.width) || nextX <= 0) {
                this.direction = nextX >= (canvasWidth - this.width) ? getRandomInt(90, 270) : getRandomInt(-90, 90);
                nextX = Math.max(0, Math.min(canvasWidth - this.width, nextX));
            }

            if (nextY >= (canvasHeight - this.height) || nextY <= 0) {
                this.direction = nextY >= (canvasHeight - this.height) ? getRandomInt(180, 360) : getRandomInt(0, 180);
                nextY = Math.max(0, Math.min(canvasHeight - this.height, nextY));
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
            const index = stars.findIndex(star => star === this);
            if (index > -1) {
                stars.splice(index, 1);
            }
        }

        update() {
            this.updatePosition();
            this.render();
        }
    }

    function instantiatePopulation() {
        for (let i = 0; i < numberOfStars; i++) {
            stars.push(new Star(i));
        }
    }

    function animate() {
        context.clearRect(0, 0, canvasWidth, canvasHeight);
        stars.forEach(star => star.update());
        requestAnimationFrame(animate);
    }

    canvas.onclick = function (e) {
        giveBirth(e, birthToGive);
    };

    function giveBirth(e, count) {
        for (let i = 0; i < count; i++) {
            const newStar = new Star(stars.length);
            newStar.x = e.offsetX - newStar.width / 2;
            newStar.y = e.offsetY - newStar.height / 2;
            stars.push(newStar);
        }
    }

    window.onload = function () {
        setCanvasSize();
        instantiatePopulation();
        animate();
    };

    window.onresize = setCanvasSize;
})();


// SOURCE: http://codepen.io/Thibka/pen/mWGxNj