---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 6
description: עמוד גלריה עם תמונות והסברים
---

<div class="gallery">
  {% for item in site.data.gallery %}
    <div class="gallery-item">
      <img 
        src="{{ site.baseurl }}/assets/img/gallery/{{ item.image }}" 
        alt="gallery image" 
        onclick="expandImage(this, '{{ item.caption | escape }}')">
    </div>
  {% endfor %}
</div>

<!-- Image modal -->
<div id="modal" class="modal" onclick="closeModal()">
  <span class="close">&times;</span>
  <img class="modal-content" id="modal-img">
  <div id="modal-caption"></div>
</div>

<style>
.gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: flex-start;
}

.gallery-item {
  width: 200px;
  text-align: center;
}

.gallery-item img {
  width: 100%;
  cursor: pointer;
  border-radius: 8px;
  transition: transform 0.3s;
}

.gallery-item img:hover {
  transform: scale(1.05);
}

.modal {
  display: none;
  position: fixed;
  z-index: 100;
  padding-top: 60px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

#modal-caption {
  text-align: center;
  margin: 20px;
  color: #fff;
  font-size: 18px;
}

.close {
  position: absolute;
  top: 20px;
  right: 35px;
  color: #fff;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}
</style>

<script>
function expandImage(img, captionText) {
  var modal = document.getElementById("modal");
  var modalImg = document.getElementById("modal-img");
  var caption = document.getElementById("modal-caption");
  modal.style.display = "block";
  modalImg.src = img.src;
  caption.innerHTML = captionText;
}

function closeModal() {
  var modal = document.getElementById("modal");
  modal.style.display = "none";
}
</script>
