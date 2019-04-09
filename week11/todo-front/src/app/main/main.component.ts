import { Component, OnInit, OnDestroy } from '@angular/core';
import {MyServiceService} from './services/my-service.service';
import {ITask,ITaskList} from './models/todo';
import { loadInternal } from '@angular/core/src/render3/util';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public taskLists:ITaskList[]=[];
  public curList:ITaskList;
  public tasks: ITask[]=[];
  public loading=true;
  constructor(private provider: MyServiceService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res=>{
      this.taskLists=res;
    });
  }
  getExList(list: ITaskList) {
    this.provider.getExactList(list.id).then(res => {
      this.curList=res;
      console.log(this.curList);
    });
  }
  getTasks(l:ITaskList){
    this.provider.getTasks(l.id).then(res=>{
      this.tasks=res;
      if (res.length>0){
        this.loading=true;
      }else{
        this.loading=false;
      }

    });
  }

  

}
