async function tryDoAction()
{
    //console.log("id of button = " +btnObj.id) //it works
    //add tryDoAction Here
    let token = sessionStorage["token"]
    let fetchParams = {method : 'POST',
    body : JSON.stringify({nothing:"nothing"}),
    headers : {"Content-Type" : "application/json",'x-access-token' : token}}

    let resp = await fetch("http://localhost:5000/actions", fetchParams); 
   let data = await resp.json();
   //alert("resp.ok=" +resp.ok)

    if(resp.ok!=true)
        redirect(data["error"],"login")
}
        async function changePage(btnObj,isSubDir=false)
        {
            //console.log("id of button = " +btnObj.id) //it works
            //add tryDoAction Here
            let token = sessionStorage["token"]
            let fetchParams = {method : 'POST',
            body : JSON.stringify({nothing:"nothing"}),
            headers : {"Content-Type" : "application/json",'x-access-token' : token}}

            let resp = await fetch("http://localhost:5000/actions", fetchParams); 
           let data = await resp.json();
           //alert("resp.ok=" +resp.ok)
            
            if(resp.ok!=true)
                {
                    if (isSubDir == true)
                        redirect(data["error"],"login")
                    else
                        redirectClient(data["error"],"login")
                } 
            else
                document.location.href = btnObj.id +".html"
        }
        function redirect(messageStr,pageStr) //sub folder redirect
        {
            strHref= "../redirect.html" + "?message="+messageStr+"&page="+pageStr
            document.location.href=strHref
        }

        function redirectClient(messageStr,pageStr) //main folder redirect
            {
                strHref= "redirect.html" + "?message="+messageStr+"&page="+pageStr
                document.location.href=strHref
            }

        function logout()
        {
            sessionStorage.removeItem("token")
            sessionStorage.clear()
            document.location.href = "login.html"
        }

        async function getUser()
        {
            let token = sessionStorage["token"]
            let data= parseJwt(token)
            console.log(data)
            //console.log(token)
            let user_id = data.user_id
            console.log(user_id)
            //let resp = await fetch("http://")
           // let resp = await fetch("http://localhost:5000/users/"+eid.toString(), {headers : {'x-access-token' : token}});
           let resp = await fetch("http://localhost:5000/users/"+user_id, {method:'GET',headers : {'x-access-token' : token}}); 
           let data2 = await resp.json();
            console.log("after request user by user id")
            console.log(data2)
            sessionStorage["user_id"] = user_id
            sessionStorage["fullname"] = data2.FullName
            txtUserFullname = document.getElementById("idFullname");
            txtUserFullname.innerText = "User Fullname: " +data2.FullName
        }

        function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}