from flet import Column,Image,ScrollMode,BoxFit,InteractiveViewer
import asyncio , os,pymupdf,gc
from typing import Optional
class PdfColumn(Column):
    """
**FLET PDF VIEW** 
**EXMEPLE CODE**: 
```
from flet_pdfview import PdfColumn
from flet import Page,run,BoxFit

def main(page:Page):
    page.add(
        PdfColumn(
            src="you/pdf/path",
            expand=True,
            dpi=300,
            fitImage=BoxFit.FILL,
            enable_zoom=True
        )
    )
run(main)
```

make sure if the path do not end with .pdf or the path not exists the PdfColumn will do not show anything !
    """
    def __init__(self,src:str="",enable_zoom:Optional[bool]=False,max_zoom:float=2.5,min_zoom:float=0.8,trackpad_scroll_causes_scale:Optional[bool]=True,widht:Optional[int]=None,height:Optional[int]=None,spacing:Optional[int]=None,expand_loose:Optional[bool]=False,expand:Optional[bool]=False,scroll:ScrollMode=ScrollMode.ADAPTIVE,dpi:int=150,fitImage:BoxFit=BoxFit.FILL,visible:Optional[bool]=True):
        super().__init__()
        self._src=src
        self.expand=expand
        self.expand_loose=expand_loose
        self.scroll=scroll
        self.spacing=spacing
        self.widht=widht
        self.height=height
        self.controls=[]
        self._fitImage=fitImage
        self._dpi=dpi
        self.visible=visible
        self._enable_zoom=enable_zoom
        self._min_zoom=min_zoom
        self._max_zoom=max_zoom
        self._trackpad_scroll_causes_scale=trackpad_scroll_causes_scale
        # self.page.run_task

    async def __start_converte(self,path:str="",dpi:int=150):
        try:
            self.controls.clear()
            if os.path.exists(path) and path.endswith(".pdf"):
                
                pdf_pages = pymupdf.open(path)
                
                for pdf_page in pdf_pages:
                    if self.src==path:
                        pix = pdf_page.get_pixmap(dpi=dpi)
                        
                        # pix.save(filename="file.png",output=ram)
                        self.controls.append(
                            InteractiveViewer(
                                expand=self.expand,
                                expand_loose=self.expand_loose,
                                width=self.widht,
                                height=self.height,              
                                content=Image(
                                    expand=self.expand,
                                    expand_loose=self.expand_loose,
                                    width=self.widht,
                                    height=self.height,
                                    src=pix.tobytes(),
                                    fit=self.fitImage
                                ),
                                scale_enabled=self._enable_zoom,
                                trackpad_scroll_causes_scale=self._trackpad_scroll_causes_scale,
                                max_scale=self._max_zoom,
                                min_scale=self._min_zoom
                                )
                            )
                        
                        self.update()
                        gc.collect()
                        del pix
                        del pdf_page
                        await asyncio.sleep(0.3)
                    else:
                        break
        except :
            self.start_function.cancel()
        finally:
            # تنظيف الذاكرة في كل الأحوال
            if 'pdf_pages' in locals():
                pdf_pages.close()
    def did_mount(self):
        if self._src:
            self.start_function = asyncio.create_task(self.__start_converte(self._src, self._dpi))
    def will_unmount(self):
        if self.start_function:
            self.start_function.cancel()
    @property
    def src(self):
        return self._src
    @src.setter
    def src(self,new_src):
        self._src=new_src
        self.start_function = asyncio.create_task(self.__start_converte(new_src,))
    @property
    def fitImage(self):
        return self._fitImage
    @fitImage.setter
    def fitImage(self,new_fitImage):
        self._fitImage=new_fitImage
        for parent_image in self.controls:
            if isinstance(parent_image,InteractiveViewer):
                image = parent_image.content
                if isinstance(image,Image):
                    image.fit=new_fitImage
    @property
    def dpi(self):
        return self._dpi
    @dpi.setter
    def dpi(self,new_dpi):
        self._dpi=new_dpi
        self.start_function = asyncio.create_task(self.__start_converte(self.src,))
    @property
    def enable_zoom(self):
        return self._enable_zoom
    @enable_zoom.setter
    def enable_zoom(self, value: bool):
        self._enable_zoom = value
        for viewer in self.controls:
            if isinstance(viewer, InteractiveViewer):
                viewer.scale_enabled = value
        self.update()
    @property
    def trackpad_scroll_causes_scale(self):
        return self._trackpad_scroll_causes_scale
    @trackpad_scroll_causes_scale.setter
    def trackpad_scroll_causes_scale(self, value: bool):
        for viewer in self.controls:
            if isinstance(viewer, InteractiveViewer):
                viewer.trackpad_scroll_causes_scale = value
    @property
    def max_zoom(self):
        return self._max_zoom
    @max_zoom.setter
    def max_zoom(self, value: float):
        for viewer in self.controls:
            if isinstance(viewer, InteractiveViewer):
                viewer.max_scale = value
    @property
    def min_zoom(self):
        return self._min_zoom
    @min_zoom.setter
    def min_zoom(self, value: float):
        for viewer in self.controls:
            if isinstance(viewer, InteractiveViewer):
                viewer.min_scale = value