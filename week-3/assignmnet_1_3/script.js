

let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
fetch(url)
.then(function(taipei){
    return taipei.json();
})
.then(function(data){
    let y = (data.result.results).length;
    let x=0;
    while(x<8){
        let title = data.result.results[x].stitle;
        let image = data.result.results[x].file;
        let image1 = image.split(/.jpg|.JPG/)[0]+".jpg";
        let mycontainer = document.getElementById("container")
        let item = document.createElement('div')
            item.classList.add('image');
        let imgbox = document.createElement('img');
            imgbox.src = image1;
            item.appendChild(imgbox);
        let titlebox = document.createElement('div');
            titlebox.classList.add('word');
            titlebox.textContent=title;
            item.appendChild(titlebox);
            mycontainer.appendChild(item);
        x += 1;
    }
})
let x=8;
function learn(){
    x+8;
    fetch(url)
    .then(function(taipei){
        return taipei.json();
    })
    .then(function(data){
        let y = (data.result.results).length;
        let count = 0;
        while(x<y && count < 8){
            let title = data.result.results[x].stitle;
            let image = data.result.results[x].file;
            let image1 = image.split(/.jpg|.JPG/)[0]+".jpg";
            let mycontainer = document.getElementById("container")
            let item = document.createElement('div')
                item.classList.add('image');
            let imgbox = document.createElement('img');
                imgbox.src = image1;
                item.appendChild(imgbox);
            let titlebox = document.createElement('div');
                titlebox.classList.add('word');
                titlebox.textContent=title;
                item.appendChild(titlebox);
                mycontainer.appendChild(item);
            x += 1;
            count +=1;
            if(x>=y){
                document.getElementById("hide").style.display = "none";
                let empty1 = document.createElement('div');
                    empty1.classList.add('image');
                let empty2 = document.createElement('div');
                    empty2.classList.add('image');
                    mycontainer.append(empty1,empty2);
            }
        }
    })
}
