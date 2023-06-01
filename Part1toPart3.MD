Part 1 (5 marks):
 
1.	Can you provide a brief summary of what is happening in this function code?
In this function code, a reducer named countReducer is defined. It takes two parameters: state and action. The reducer is responsible for updating the state based on the action type. The state parameter is assigned a default value of initialState, which represents the initial state of the application.
Inside the function, it checks if the action.type is equal to 'increment'. If the condition is true, it returns a new state object with the value property incremented by 1.
If the action.type is not 'increment', it simply returns the current state unchanged.

2.	Add one action that tells the reducer to reduce the state value by 1
function countReducer(state = initialState, action) {
    if (action.type === 'increment') {
      return {
        value: state.value + 1,
      };
    } else if (action.type === 'decrement') {
      return {
        value: state.value - 1,
      };
    }
    return state;
  }
  

3.	Add one action that tells the reducer to reset the state
function countReducer(state = initialState, action) {
    if (action.type === 'increment') {
      return {
        value: state.value + 1,
      };
    } else if (action.type === 'decrement') {
      return {
        value: state.value - 1,
      };
    } else if (action.type === 'reset') {
      return initialState;
    }
    return state;
  }

 
Part 2 (10 marks):
 
This section involves handling state locally.
 
In the code above the useState hook is used to set the state of a variable inside the component.
1.	Can you provide a brief summary on what is happening on line 34, 39?
In lines 34-39 of  the code , we have a functional component called classInfo. Inside this component, there is a state variable called studentsCount, which is initially set to 0 using the useState hook. This variable will keep track of the number of students present in the class.

The component returns a JSX element, which is a <div> container. Inside this container, there is a <p> tag that displays the current value of studentsCount using string interpolation. This allows the value to be updated and shown on the screen. Below the <p> element, there is a <button> tag labeled "Add Student" with an onClick event handler. Currently, the event handler is empty and marked as ????, which indicates that it needs to be filled with a function. This function will be called when the button is clicked and will perform the desired action, such as updating the studentsCount state or executing some additional logic.
 
2.	When a user clicks on the “Add student” button update the state (studentsCount) to include only the total number of students who are present. Using the data provided below:
 
Figure 3
a.	Write a pseudocode of how your function would look.
const classInfo = () => {
    const [studentsCount, setStudentsCount] = useState(0);
  
    const handleAddStudent = () => {
      const presentStudents = students.filter(student => student.present);
      setStudentsCount(presentStudents.length);
    };
  
    const students = [
      { name: "Nrupul", present: false },
      { name: "Prateek", present: true },
      { name: "Jane", present: true },
      { name: "Paul", present: false },
      { name: "Luke", present: true },
    ];
  
    return (
      <div>
        <p>Number of students in the classroom: {studentsCount}</p>
        <button onClick={handleAddStudent}>Add Student</button>
      </div>
    );
  };
  

b.	How do you ensure that the function is triggered when the button is clicked?
 
To make sure the function gets triggered when I click the button, I assign the function as an event handler to the onClick attribute of the button element. I use the handleAddStudent function as the event handler for the onClick attribute of the button element. When I click the button, the handleAddStudent function gets called, which makes the logic inside it run. This logic increments the studentsCount state by 1 using setStudentsCount(studentsCount + 1).


c.	How will you update the state with the result of your function?
 
To update the state with the result of my function, I use the setStudentsCount function provided by the useState hook. Inside my handleAddStudent function, I filter the students array to find only the students who are present. I count the number of present students by checking if student.present is true. This count is stored in the presentStudents array.

To update the state, I call setStudentsCount(presentStudents.length). This sets the value of the state variable studentsCount to the number of present students. By calling setStudentsCount with the new value, the state variable studentsCount gets updated. As a result, the component is re-rendered, and I can see the updated state value.

By using setStudentsCount with the count of present students, I update the state to reflect the result of my function. This triggers a re-render of the component with the updated state value displayed. 
 
#Part 3 (10 marks):
 
Now let’s use dispatch to update the state on button click
 
1.	A change of code was made on line 174 (figure 4), can you briefly explain what that would do?
 
The change of code on line 174, value: state.value + action.payload, will update the value property of the state by adding the value of action.payload to the current value.
For example, if the current state is { value: 5 } and the action being dispatched has a payload value of 2, the code change on line 174 will result in the updated state being { value: 7 }.
So, the change on line 174 performs an increment operation on the value property of the state by adding the value from action.payload to the existing state.value.

2.	Let’s say we don’t want to set the state locally anymore and want to use dispatch. How would you ensure that an “increment” action that also contains the result of the studentCount is dispatched on button click? According to your answer in part 2.2b what would need to be changed?
 
To ensure that we are no longer setting the state locally and implementing useDispatch, the following changes would need to be made. First, the useDispatch function from React-Redux should be imported. Then, the useState hook for studentsCount and the setStudentsCount function should be removed. Next, a handleAddStudent function should be created, which calculates the studentCount based on the present students in the students array. Inside this function, an action object should be defined with the type set as 'increment' and the studentCount as the payload. The useDispatch hook should be utilized to obtain the dispatch function. The action should be dispatched within the handleAddStudent function using the dispatch function. Finally, the handleAddStudent function should be assigned as the event handler for the onClick attribute of the button element

An Example of how the code would look:
  import { useDispatch } from 'react-redux';

  const ClassInfo = () => {
    const dispatch = useDispatch();
    
    const handleAddStudent = () => {
      const presentStudents = students.filter(student => student.present);
      const studentCount = presentStudents.length;
      
      const action = {
        type: 'increment',
        payload: studentCount
      };
  
      dispatch(action);
    };
    
    const students = [
      { name: "Nrupul", present: false },
      { name: "Prateek", present: true },
      { name: "Jane", present: true },
      { name: "Paul", present: false },
      { name: "Luke", present: true },
    ];
  
    return (
      <div>
        <p>Number of students in the classroom: {studentsCount}</p>
        <button onClick={handleAddStudent}>Add Student</button>
      </div>
    );
  };
  
  export default ClassInfo;
  

3.	Which code do you think is best suited to ensure that the “increment” action updates the state with the correct total number of students who are present. Is it Figure 4? Or
Figure 5? Explain the code difference and your reasoning
 
Based on our desired goal, I feel the code in Figure 4 is better suited to ensure that the increment action updates the state with the correct total number of students who are present.

This is because the code inside the increment condition of the reducer adds the value of action.payload to the existing state.value. This ensures that the state is updated by incrementing the value correctly based on the payload value.

Whereas in Figure 5, the code inside the "increment" condition of the reducer only sets the value of the state to the value of action.payload. As a result this replaces the existing value with the payload value, rather than incrementing it based on the payload.

Considering the objective of updating the state with the total number of students who are present, it is apparent Figure 4 presents a more suitable solution as it correctly increments the value of the state based on the payload value, this ensures that the state reflects the accurate total count.
