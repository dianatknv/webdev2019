import { Injectable } from '@angular/core';
import {ExService} from './ex.service';
import {HttpClient} from '@angular/common/http';
import {ITask,ITaskList} from '../models/todo'
@Injectable({
  providedIn: 'root'
})
export class MyServiceService extends ExService {

  constructor(http:HttpClient) {
    super(http);
   }
   getTaskLists(): Promise<ITaskList[]>{
     return this.get(`http://127.0.0.1:8000/api/task_lists/`,{});
   }
   getExactList(id: number): Promise<ITaskList>{
     return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/`,{id});
   }
   getTasks(id: number): Promise<ITask[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/tasks/`, {id});
  }
}
