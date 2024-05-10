import React, { useState, useEffect } from 'react';
import Axios from 'axios';

const HomePage = () => {
  const [districts, setDistricts] = useState([]);
  const [subdivisions, setSubdivisions] = useState([]);
  const [selectedDistrict, setSelectedDistrict] = useState('');
  const [selectedSubdivision, setSelectedSubdivision] = useState('');
   
  const [isLoadingDistricts, setLoadingDistricts] = useState(true);
  const [isLoadingSubdivisions, setLoadingSubdivisions] = useState(true);

  const [blocks, setBlocks] = useState([]);
  const [selectedBlock, setSelectedBlock] = useState('');
  const [isLoadingBlocks, setLoadingBlocks] = useState(true);





  useEffect(() => {
    if (selectedSubdivision) {
      setLoadingBlocks(true);
      const fetchBlocks = async () => {
        try {
          const response = await Axios.get(`http://127.0.0.1:8000/load/listblocks/${selectedSubdivision}`);
          setBlocks(response.data);

          
          setLoadingBlocks(false);
          

        } catch (error) {
          console.error('Error fetching blocks:', error);
        }
      };
      fetchBlocks();
    }
  }, [selectedSubdivision]);
  const [name, setName] = useState('');

  useEffect(() => {
    setLoadingDistricts(true);
    const fetchDistricts = async () => {
      try {
        const response = await Axios.get('http://127.0.0.1:8000/load/listdistricts/');
        setDistricts(response.data);
        
        setLoadingDistricts(false);
        //console.log('districtid : ',selectedDistrict)
      } catch (error) {
        console.error('Error fetching districts:', error);
      }
    };
    fetchDistricts();
  }, []);

  useEffect(() => {
    if (selectedDistrict) {
      setLoadingSubdivisions(true);
      const fetchSubdivisions = async () => {
        try {
          const response = await Axios.get(`http://127.0.0.1:8000/load/listsubdivs/${selectedDistrict}`);
          setSubdivisions(response.data);
          setLoadingSubdivisions(false);
        } catch (error) {
          console.error('Error fetching subdivisions:', error);
        }
      };
      fetchSubdivisions();
    }
  }, [selectedDistrict]);

 
  const handleChangeDistrict = (event) => {
    setSelectedDistrict(event.target.value);
    setSelectedSubdivision('');
  };

  const handleChangeSubdivision = (event) => {
    setSelectedSubdivision(event.target.value);
  };

  const handleChangeBlock = (event) => {
    setSelectedBlock(event.target.value);
  };
  
  const handlenamechange =(event)=>{
    setName(event.target.value);
      };




      const handlesubmit = async (event) => {
        event.preventDefault();
        const inputData = name.trim()
       // console.log(inputData)
        try {
          const response = await Axios.get(`http://127.0.0.1:8000/load/generatespin/${selectedSubdivision}`);
          const { subdivision_id, id,unique_number  } = response.data;
          
          if(selectedDistrict === 'Gangtok'){
            console.log('spin id for ',inputData,' :',`SK01/${subdivision_id}/${id}/${unique_number}`)
           }
           if(selectedDistrict === 'Mangan'){
            console.log(`SK03/${subdivision_id}/${id}/${unique_number}`)
           }
           if(selectedDistrict === 'Gyalshing'){
            console.log(`SK02/${subdivision_id}/${id}/${unique_number}`)
           }
           if(selectedDistrict === 'Namchi'){
            console.log(`SK04/${subdivision_id}/${id}/${unique_number}`)
           }
           if(selectedDistrict === 'Pakyong'){
            console.log(`SK07/${subdivision_id}/${id}/${unique_number}`)
           }
           if(selectedDistrict === 'Soreng'){
            console.log(`SK06/${subdivision_id}/${id}/${unique_number}`)
           }
          
        } catch (error) {
          console.error('Error generating SPIN ID:', error);
        }
      };    

  
  

  return (
    <div className="page">


      <h2>details</h2>
      <form className="form">
      <input
            type="text"
            placeholder="Enter Name"
            onChange={handlenamechange}
          />
        <label>
          District
          <select value={selectedDistrict} onChange={handleChangeDistrict}>
            <option value="">Select District</option>
            {isLoadingDistricts ? (
              <option value="Loading" disabled>Loading.....</option>
            ) : (
              districts.map((district, index) => (
                <option key={index} value={district}>
                  {district}
                </option>
              ))
            )}
          </select>
        </label>
        <label>
          Subdivision
          <select value={selectedSubdivision} onChange={handleChangeSubdivision}>
            <option value="">Select Subdivision</option>
            {isLoadingSubdivisions ? (
              <option value="Loading" disabled>Loading.....</option>
            ) : (
              subdivisions.map((subdivision, index) => (
                <option key={index} value={subdivision}>
                  {subdivision}
                </option>
              ))
            )}
          </select>
          </label>

          <label>
          Block
          <select value={selectedBlock} onChange={handleChangeBlock}>
            <option value="">Select Block</option>
            {isLoadingBlocks ? (
              <option value="Loading" disabled>Loading.....</option>
            ) : (
              blocks.map((block, index) => (
                <option key={index} value={block}>
                  {block}
                </option>
              ))
            )}
          </select>
        </label>
        <button type="submit" onClick={handlesubmit}>Submit</button>
      </form>
    </div>
  );
};

export default HomePage;
