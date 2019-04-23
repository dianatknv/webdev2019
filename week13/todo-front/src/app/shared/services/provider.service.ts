import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import { IAuthResponse, TaskList, Task } from '../models/model';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
  }

  getTasksList(): Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/tasklist/', {});
  }

  createTaskList(name: any): Promise<TaskList> {
    return this.post('http://localhost:8000/api/tasklist/', {
      name
    });
  }
  updateTaskList(tasklist: TaskList): Promise<TaskList> {
    return this.put(`http://localhost:8000/api/tasklist/${tasklist.id}/`, {
      name : tasklist.name
    });
  }
  deleteTaskList(tasklist: TaskList): Promise<TaskList> {
    return this.delet(`http://localhost:8000/api/tasklist/${tasklist.id}/`, {});
  }
  getTasks(id: number): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/tasklist/${id}/task/`, {});
  }
  updateTask(task: Task): Promise<Task> {
    return this.put(`http://localhost:8000/api/tasklist/${task.task_list.id}/task/`, {
      name: task.name,
      status: task.status,
      created_at: task.created_at,
      due_on: task.due_on,
      task_list: task.task_list
    });
  }
  createTask(tname: string, createdat: Date, dueon: Date, tstatus: string, tasklist: number): Promise<Task> {
    return this.post(`http://localhost:8000/api/tasklist/${tasklist}/task/`, {
      name: tname,
      created_at: createdat,
      due_on: dueon,
      status: tstatus,
      task_list: tasklist
    });
  }
  deleteTask(task: Task) {
    return this.delet(`http://localhost:8000/api/tasklist/${task.task_list.id}/task/${task.id}/`, {});
  }
  auth(uname: string, pword: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: uname,
      password: pword
    });
  }
  logout(): Promise<any> {
    return this.post(`http://localhost:8000/api/logout/`, {});
  }
}
