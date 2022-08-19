
<?php 
$json ='[{ "name": "Royal Challengers Bangalore", "location": "Bangalore", "player": [ { "name": "Faf Du Plessis", "country": "South Africa", "role": "Batsman", "price-in-crores": "7" }, { "name": "Virat Kohli", "country": "India", "role": "Batsman", "price-in-crores": "15" }, { "name": "Glenn Maxwell", "country": "Australia", "role": "Batsman", "price-in-crores": "11" }, { "name": "Mohammad Siraj", "country": "India", "role": "Bowler", "price-in-crores": "7" }, { "name": "Harshal Patel", "country": "India", "role": "Bowler", "price-in-crores": "10.75" }, { "name": "Wanindu Hasaranga", "country": "Srilanka", "role": "Bowler", "price-in-crores": "10.75" }, { "name": "Dinesh Karthik", "country": "India", "role": "Wicket-keeper", "price-in-crores": "5.5" }, { "name": "Shahbaz Ahmed", "country": "India", "role": "All-Rounder", "price-in-crores": "2.4" }, { "name": "Rajat Patidar", "country": "India", "role": "Batsman", "price-in-crores": "0.20" }, { "name": "Josh Hazlewood", "country": "Australia", "role": "Bowler", "price-in-crores": "7.75" }, { "name": "Mahipal Lomror", "country": "India", "role": "Bowler", "price-in-crores": "7.75" } ]}]';
 
 

 
$meg = json_decode($json, true);

      echo display_array_recusive($meg);

function display_array_recusive($json_rec){

		foreach($json_rec as $key =>$value){
			if( is_array($value)){
			display_array_recusive($value);	
				
				
			}else{
				if($value !== "India" &&  $value <=4 ){
				echo'<pre>';
				echo $key ."   ".$value."";
				
				
				echo'</pre>';
				}
			}
			
			
	
		
		
		
		
	}
	
}
echo "wicket keeper  display "; 


echo display_array_recusive1($meg);

function display_array_recusive1($json_rec1){

		foreach($json_rec1 as $key =>$value){
			if( is_array($value)){
			display_array_recusive1($value);	
				
				
			}else{
				
				
				if($value  == "Wicket-keeper"){
				
				echo $key ."   ".$value."";
				
				
				
				}
			}
			
			
	
		
		
		
		
	}
	
}
?> 