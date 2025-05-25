import React from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider,createBrowserRouter } from 'react-router-dom';

import { TitlePart } from './titlePages/titlePage';
import { LoginPart } from './titlePages/loginPage';
import { SignupPart } from './titlePages/signPage';

import { ShoppingList } from './userPages/shoppingList';
import { BookList } from './userPages/bookList';
import { TodoList } from './userPages/todoList';
import { UserHeader } from './userPages/userHeader';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

const router=createBrowserRouter([
  {path: '/', element: <TitlePart/>},
  {path: '/login', element: <LoginPart/>},
  {path: '/signup', element: <SignupPart/>},
  {path: '/user', element:<UserHeader/>,children:[
    {path: 'shopping_list', element: <ShoppingList/>},
    {path: 'book_list', element: <BookList/>},
    {path: 'todo_list', element: <TodoList/>}
  ]}
])

root.render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);

