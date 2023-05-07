import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MAT_FORM_FIELD_DEFAULT_OPTIONS } from '@angular/material/form-field';
import { AllMaterialStuffModule } from '../material.module';

import { AppComponent } from './app.component';
import { EditorComponent } from './editor/editor.component';

import { RadioEditorComponent } from './radio-editor/radio-editor.component';
import { EditableLabelComponent } from './editable-label/editable-label.component';

const routes: Routes = [
  { path: '', component: EditorComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    EditorComponent,
    RadioEditorComponent,
    EditableLabelComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot(routes),
    BrowserAnimationsModule,
    AllMaterialStuffModule
  ],
  providers: [
    { provide: MAT_FORM_FIELD_DEFAULT_OPTIONS, useValue: { appearance: 'outline' } }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
