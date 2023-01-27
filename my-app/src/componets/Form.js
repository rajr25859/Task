import React, { useState ,useEffect} from "react";
import {Link, useNavigate} from 'react-router-dom';

function Form(props) {
  const [value, setValue] = useState({
    name:"",
    age:"",
    gender:"",
  });

  const navigate = useNavigate();


  function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData();

    Object.entries(value).forEach(([key, value]) => {
      formData.append(key, value);
      console.log("key-", key, "-----", "value-", value)
      
    }); 
    navigate('/grid',{state:{name:value.name,
      age:value.age,
      gender:value.gender,}});

  
  }


  function handleChange(e) {
    const name = e.target.name;
    const value = e.target.value;
    setValue((formProps) => ({
      ...formProps,
      [name]: value,
    }));
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2 className="label-wrapper">
        <label htmlFor="new-todo-input" className="label__lg">
         Demo Form
        </label>
      </h2>
      <div>
      <input
        type="text"
        id="new-todo-input"
        className="input input__lg"
        name="name"
        autoComplete="off"
        placeholder="FULL NAME"
        value={value.name}
        onChange={handleChange}
      />
      </div>
       <div>
      <input
        type="number"
        id="new-todo-input"
        className="input input__lg"
        placeholder="AGE"
        name="age"
        autoComplete="off"
        value={value.age}
        onChange={handleChange}
        required
      />
  </div>
  <div>
      <select
        name="gender"
        required
        value={value.gender}
        onChange={handleChange}
      
      >
       
        <option value="Male">Male</option>
        <option value="Female">Female</option>
        <option value="Other">Other</option>
      </select>
      </div>
      <div>
      <button type="submit" className="btn btn__primary btn__lg">
      submit
      </button>
      </div>
    </form>
  );
}

export default Form;