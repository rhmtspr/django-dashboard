document.addEventListener("DOMContentLoaded",(function(){var e,t=document.getElementById("calendar"),n=document.getElementById("drop-remove"),d=document.getElementById("modal-title"),l=document.getElementById("form-event"),a=null,o=null,r=document.getElementsByClassName("needs-validation"),s=new Date,m=s.getDate(),i=s.getMonth(),c=s.getFullYear(),u=[{title:"All Day Event",start:new Date(c,i,1),className:"w-[100%] text-purple-500 !bg-purple-100 dark:!bg-purple-500/20 border-none rounded-md py-1.5 px-3"},{title:"Long Event",start:new Date(c,i,m-5),end:new Date(c,i,m-2),className:"!text-sky-500 w-[100%] !bg-sky-100 dark:!bg-sky-500/20 border-none rounded-md py-1.5 px-3"},{id:999,title:"Repeating Event",start:new Date(c,i,m-3,16,0),allDay:!1,className:"text-yellow-500 w-[100%] !bg-yellow-100 dark:!bg-yellow-500/20 border-none rounded-md py-1.5 px-3"},{id:999,title:"Repeating Event",start:new Date(c,i,m+4,16,0),allDay:!1,className:"w-[100%] text-custom-500 !bg-custom-100 dark:!bg-custom-500/20 border-none rounded-md py-1.5 px-3"},{title:"Meeting",start:new Date(c,i,m,10,30),allDay:!1,className:"text-green-500 w-[100%] !bg-green-100 dark:!bg-green-500/20 border-none rounded-md py-1.5 px-3"},{title:"Lunch",start:new Date(c,i,m,12,0),end:new Date(c,i,m,14,0),allDay:!1,className:"text-purple-500 w-[100%] !bg-purple-100 dark:!bg-purple-500/20 border-none rounded-md py-1.5 px-3"},{title:"Birthday Party",start:new Date(c,i,m+1,19,0),end:new Date(c,i,m+1,22,30),allDay:!1,className:"w-[100%] text-sky-500 !bg-sky-100 dark:!bg-sky-500/20 border-none rounded-md py-1.5 px-3"},{title:"Click for Google",start:new Date(c,i,28),end:new Date(c,i,29),url:"http://google.com/",className:"w-[100%] text-custom-500 !bg-custom-100 dark:!bg-custom-500/20 border-none rounded-md py-1.5 px-3"}];(e=new FullCalendar.Calendar(t,{timeZone:"UTC",editable:!0,droppable:!0,selectable:!0,initialView:"multiMonthYear",themeSystem:"tailwindcss",headerToolbar:{left:"prev,next,today",center:"title",right:"dayGridMonth,timeGridWeek,timeGridDay,listMonth"},drop:function(e){n.checked&&e.draggedEl.parentNode.removeChild(e.draggedEl)},windowResize:function(e){},eventDidMount:function(e){if("done"===e.event.extendedProps.status){e.el.style.backgroundColor="red";var t=e.el.getElementsByClassName("fc-event-dot")[0];t&&(t.style.backgroundColor="white")}},eventClick:function(e){document.getElementById("event-modal").classList.remove("hidden"),document.getElementById("calendarBtn").click(),l.reset(),document.getElementById("event-title").value="",a=e.event,document.getElementById("event-title").value=a.title,document.getElementById("event-category").value=a.classNames[0],o=null,document.getElementById("btn-delete-event").classList.remove("hidden"),document.getElementById("btn-save-event").innerText="Edit Event",o=null},dateClick:function(e){!function(e){l.classList.remove("was-validated"),l.reset(),a=null,d.innerText="Add Event",o=e}(e),document.getElementById("event-modal").classList.remove("hidden"),document.getElementById("calendarBtn").click()},events:u})).render(),l.addEventListener("submit",(function(t){t.preventDefault();var n=document.getElementById("event-title").value,d=document.getElementById("event-category").value;if(!1===r[0].checkValidity())r[0].classList.add("was-validated");else{if(a)a.setProp("title",n),a.setProp("classNames",[d]);else{var l={title:n,start:o.date,allDay:o.allDay,className:d};e.addEvent(l)}document.getElementById("eventModal-close").click()}})),document.getElementById("btn-delete-event").addEventListener("click",(function(e){a&&(a.remove(),a=null,document.getElementById("eventModal-close").click())}))}));