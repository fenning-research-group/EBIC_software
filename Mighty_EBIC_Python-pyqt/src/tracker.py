import matplotlib
import numpy
#import WriteToHdf5
import scanUpdate, edm
import thread, Queue
import config
import scanobject
import Mfigure
import pylab
from scipy import mgrid
from time import strftime
from Mexport import Exporter
from pyqtgraph import QtCore


class GuiTracker:
    def __init__(self, mainUI):
        self.mainUI = mainUI

    def print_poo(self):

        print 'poo'

    def getBounds(self):
	bounds =  self.mainUI.scanTracker.figTracker.activeCh.canvas.ax.viewLim.bounds   
        self.mainUI.xstartV, self.mainUI.ystartV, self.mainUI.xdeltaV, self.mainUI.ydeltaV = bounds
        self.mainUI.xstart.setText('{0:0.2f}'.format(self.mainUI.xstartV))
        self.mainUI.xdelta.setText('{0:0.2f}'.format(self.mainUI.xdeltaV))
        self.mainUI.ystart.setText('{0:0.2f}'.format(self.mainUI.ystartV))
        self.mainUI.ydelta.setText('{0:0.2f}'.format(self.mainUI.ydeltaV))

        print 'water is not good patrick'

	return bounds





class ScanTracker:
    """
    keeps track of the active scan updates evrything and replots if changed. keep track of active Figures and their active subplots, axes, plots
    updates them when needed
   
    """
    def __init__(self, mainUI):
        self.mainUI = mainUI
        self.scans =[]
        self.figTracker = FigTracker(self.mainUI)


    def display_scan(self, index = None):
        CH = self.figTracker.CH
        if index is not None:
            self.activeScan = self.scans[index]
            self.figTracker.set_active_scan(self.activeScan)
        if self.activeScan.figures is None:
            self.activeScan.figures = [] #add figures to the scan if it has None
            for i in range(len(self.activeScan.gain)):
                self.figTracker.init_figure(i)
        else:
            self.figTracker.replot_scan()        
        self.figTracker.activeChannel(CH)

    def save(self):
            scanobject.scanObjectUtils.pickle_scanobject(self.activeScan , '../data' + self.activeScan.name)


#TODO: figure out init and what should be called first
class FigTracker:
    """
    keeps track of the active Figures and their active subplots, axes, plots
    updates them when needed
    """
    def __init__(self, mainUI):
        self.mainUI = mainUI
        self.cmap = pylab.cm.Greys_r
        self.cmap_r = False
        self.set_plot_scan_alpha()
        self.set_profile_alpha()
        self.CH = 0

    #Functions for call backs sets up from main loop when things change

    def set_active_scan(self, active_scan):
        self.activeScan = active_scan


        #sets the axis and supblot index from the mainUI
    def set_axis_index(self,value = None):
        self.axis_index = self.mainUI.AxisCombo.currentIndex()
        self.set_axobject()
        self.set_ax()
        #Show active plots when the axis index changes
        self.show_active_plots_list()
        self.set_active_plots_index()

        
    def set_sub_index(self, value = None):
        self.sub_index = self.mainUI.SubPlotComobo.currentIndex()
        #show the active axes when the sub index changes
        self.show_active_axes(self.sub_index)
        self.set_subplot()


        #current plot that is active
    def set_active_plots_index(self, value = None):
        self.active_plots_index = self.mainUI.ActivePlotsCombo.currentIndex()
        if value != None and value >= 0:
            self.set_active_plot()
            self.update_hist()

    def set_active_plot(self):
        self.active_plot = self.axobject.axesObjects[self.active_plots_index]

    def set_ax(self):
        self.ax = self.activeCh.canvas.subplots[self.sub_index].axes[self.axis_index]

    def set_axobject(self):
        self.axobject = self.activeScan.figures[self.CH].subplots[self.sub_index].axes[self.axis_index]

    def set_subplot(self):
        self.subplot = self.activeCh.canvas.subplots[self.sub_index]

    def change_cmap(self, value):
        self.cmapvalue = value
        #maybe limitnumber in list with th _r??
        if self.cmap_r == True:
            self.cmap = self.mainUI.cmapList[self.cmapvalue]#pylab.cm._cmapnames[self.cmapvalue]+'_r'
        else:
            self.cmap = self.mainUI.cmapList[self.cmapvalue]#pylab.cm._cmapnames[self.cmapvalue]
        self.remove_from_plot()  #replots if changed
        self.add_image()


    def reverse_cmap(self, value):
        if  int(value) == 2:
            self.cmap_r = True
        else:
            self.cmap_r = False
        self.change_cmap(self.cmapvalue)


    def set_plot_scan_alpha(self):
        self.plot_scan_alpha = self.mainUI.PlotScansSpinAlpha.value()

    def set_plot_scan_ch(self):
        self.plot_scan_ch = self.mainUI.PlotScansComboCH.currentIndex()

    def set_profile_index(self):
        self.profile_index = self.mainUI.PlotProfileCombo.currentIndex()

    def set_profile_ch(self):
        self.profile_ch = self.mainUI.PlotProfileComboCH.currentIndex()

    def set_profile_alpha(self):
        self.profile_alpha = self.mainUI.PlotProfileAlpha.value()


    def add_subplot(self):
        CH = self.CH
        print "current CH is", CH
        temp = self.activeScan.figures[self.CH]
        if len(temp.subplots) < 2:    
            temp.add_subplot()
            if len(self.activeCh.canvas.subplots) == 1:
                self.activeCh.canvas.twoSubplots()
        self.show_subplots_axes(self.CH)
        self.replot_figure(temp.subplots)
        print "current CH is", CH
        self.activeChannel(CH)


    def add_ax(self):        
        CH = self.CH
        print "current CH is", CH
        temp = self.activeScan.figures[CH]
        #plot_index = self.AxisCombo.currentIndex()
        #print 'plot_index', plot_index
        #sub_index = self.mainUI.SubPlotComobo.currentIndex()
        #print 'sub_index', sub_index
        subplot = self.activeCh.canvas.subplots[self.sub_index]
        mSubplot = temp.subplots[self.sub_index]
        if  0 < len(mSubplot.axes) < 2:
            mSubplot.add_axes()
            axes = subplot.axes
            ax = axes[-1]
            self.activeCh.canvas.add_Ax(ax = ax, axes = axes)
            self.show_active_axes(self.sub_index)
        print "current CH is", CH
        self.activeChannel(CH)


    def replot_figure(self, temp):
        CH = self.CH
        if len(temp) == 1:
            self.activeCh.canvas.oneSubPlot()
        elif len(temp) == 2 :
            self.activeCh.canvas.twoSubplots()
        else :
            print 'fail to replot_scan'
            return
        for k in range(len(temp)):
            axes = temp[k].axes
            print 'k', k
            for l in range(len(axes)):
                print 'l', l
                if l > 0:
                    temp_axes = self.activeCh.canvas.subplots[k].axes
                    ax = temp_axes[-1]
                    ax.clear()
                    self.activeCh.canvas.add_Ax(ax = ax, axes = temp_axes)
                axobject = axes[l]
                self.activeCh.canvas.add_plotter(ax = self.activeCh.canvas.subplots[k].axes[l], axBox = axobject
                                                    , subplot = self.activeCh.canvas.subplots[k] )
                print 'added plotter in replot' , k ,l
        


    def replot_scan(self):
        """
        replots a scan if active scan is changed, or a scan is opened
        """
        #TODO: need to clear all figures before replot
        
        #print 'replot Called'
        for i in range(len(self.activeScan.figures)):
            temp = self.activeScan.figures[i].subplots
            self.activeChannel(i)
            #TODO:prototype of more scalable subplot replot for n subplots.
            #subplots should have added variable to keep track of position 111, 211, 212 etc..
            #self.activeCh.canvas.addSubplots(len(temp))
            self.replot_figure(temp)            
        self.show_subplots_axes(self.CH)


    def init_figure(self, i):
        """
        used if no figure yet exist for scan
        """
        self.activeScan.figures.append(Mfigure.FigureBox())
        axobject = self.activeScan.figures[-1].subplots[-1].axes[-1]
        self.activeChannel(i)
        self.activeCh.canvas.oneSubPlot()
        subplot = self.activeCh.canvas.subplots[-1]
        if len(axobject.axesObjects) == 0:
            name = 'Image' + 'Ch' + str(i) + self.activeScan.name
            axobject.axesObjects.append(Mfigure.ImageBox(data = self.activeScan.DisplayArray[:,:,i]
                                        , extent = self.activeScan.extent, cmap = self.cmap, origin='lower', name = name))
            print "added an axesObject:", name
        self.activeCh.canvas.add_plotter(self.activeCh.canvas.ax, axobject, subplot )
        self.show_active_plots_list(i) 




    def add_image(self):
        #TODO:will add this to command tracker and support  for N figures
        self.check_fig_active()
        name = 'Image' + 'Ch' + str(self.plot_scan_ch) + self.activeScan.name
        self.axobject.axesObjects.append(Mfigure.ImageBox(data = self.activeScan.DisplayArray[:,:,self.plot_scan_ch]
                                        , extent = self.activeScan.extent, cmap = self.cmap, origin='lower'
                                        , name = name, alpha = self.plot_scan_alpha))
        if len(self.subplot.plotters) == 0:
            self.activeCh.canvas.add_plotter(self.ax, self.axobject, self.subplot )
        else:
            plotter = self.activeCh.canvas.subplots[self.sub_index].plotters[self.axis_index]
            plotter.show_image(self.axobject.axesObjects[-1])          
        self.show_active_plots_list()   
  

    def add_line(self):
        #TODO:will add this to command tracker and support  for N figures
        self.check_fig_active()
        temp = self.activeScan.profiles[self.profile_index]
        name = temp.name + 'Ch' + str(self.profile_ch) + self.activeScan.name
        self.axobject.axesObjects.append(Mfigure.LineBox(Xdata = temp.Xposition 
                                    ,Ydata = temp.profileDataAvg[:,self.profile_ch]
                                    , name = name, alpha = self.profile_alpha))
        if len(self.subplot.plotters)- 1 < self.axis_index:
            self.activeCh.canvas.add_plotter(self.ax, self.axobject, self.subplot )
        else:
            plotter = self.activeCh.canvas.subplots[self.sub_index].plotters[self.axis_index]
            plotter.show_line(self.axobject.axesObjects[-1])          
        self.show_active_plots_list()

   
    def check_fig_active(self):
        """
        if no active figure in scan make one
        """
        if len(self.activeScan.figures) -1 < self.CH:
            self.activeScan.figures.append(Mfigure.FigureBox())
        self.set_axobject()


    def remove_from_plot(self):
        plotter = self.activeCh.canvas.subplots[self.sub_index].plotters[self.axis_index]
        plot = plotter.activeplots[self.active_plots_index]
        plotter.remove_and_update(plot)
        self.show_active_plots_list()

    def add_colorbar(self):
        plotter = self.activeCh.canvas.subplots[self.sub_index].plotters[self.axis_index]
        image = plotter.activeplots[self.active_plots_index]
        plotter.add_colorbar(image)


     
    
    #TODO: figure out if this is the right format to get it to work for us
    def show_active_plots_list(self, index = None):
        """
        shows the active plots in the figure
        """
        self.mainUI.ActivePlotsCombo.clear()
        for m in range(len(self.axobject.axesObjects)):
            #print "m in show_activeplots", m   #TODO: figure out why this is called so much
            temp = self.axobject.axesObjects[m]
            self.mainUI.ActivePlotsCombo.addItem(temp.name)


    def show_subplots_axes(self, index = None):
        temp = self.activeScan.figures[index]
        self.mainUI.SubPlotComobo.clear()
        for i in range(0, len(temp.subplots)):
            self.mainUI.SubPlotComobo.addItem(str(i))
        self.set_sub_index()


    def show_active_axes(self, index = None):
        self.mainUI.AxisCombo.clear()
        temp = self.activeScan.figures[self.CH].subplots[index]
        for k in range(len(temp.axes)):
            #print "active index", k
            self.mainUI.AxisCombo.addItem(str(k))
        self.set_axis_index()


    def update_hist(self, dump = None):
        ax = self.mainUI.HistWidget.canvas.ax
        ax.clear()
        fig = ax.get_figure()
        fig.subplots_adjust(right = 1 , left = 0)
        if self.active_plot.__class__ == Mfigure.ImageBox:
            #TODO use built in histgram of imagebox insted of computing each time
            ax.plot(self.active_plot.binHistTrunk,self.active_plot.binx)
            #ax.set_axis_off()TODO put this in and expand figure to take up hole canvas
            #ax.axis('off')
            ax.tick_params(direction = 'out', top = 'off', right = 'off', left ='off')
            ax.axes.get_yaxis().set_visible(False)
        self.mainUI.HistWidget.canvas.draw()


    def update_clim(self, dump = None):
        plotter = self.activeCh.canvas.subplots[self.sub_index].plotters[self.axis_index]
        image = plotter.activeplots[self.active_plots_index]
        if self.active_plot.__class__ == Mfigure.ImageBox:
            vmin = self.active_plot.binHist[self.mainUI.SliderVmin.value()]
            vmax = self.active_plot.binHist[self.mainUI.SliderVmax.value()]
            image.set_clim(vmin,vmax)
            self.active_plot.clim = (vmin, vmax)
            self.activeCh.canvas.draw()


    def activeChannel(self, value):

        if value == 0:
            self.activeCh = self.mainUI.mplCh1
            self.CH = 0
        elif value == 1:
            self.activeCh = self.mainUI.mplCh2
            self.CH = 1
        elif value == 2:
            self.activeCh = self.mainUI.mplCh3
            self.CH = 2
        elif value == 3:
            self.activeCh = self.mainUI.mplCh4
            self.CH = 3
        elif value == 4:
            self.activeCh = self.mainUI.mplCh5
            self.CH = 4
        elif value == 5:
            self.activeCh = self.mainUI.mplCh6
            self.CH = 5
        else :
            self.activeCh = self.mainUI.mplCh1
            self.CH = 0
        self.update_activeplots_info(self.CH)


    def update_activeplots_info(self, chindex):
        """
        when called will show everything that has been changed with the plot
        """
        if len(self.activeCh.canvas.subplots) != 0:
            self.show_subplots_axes(chindex)


    def clear_all_figures(self):
        """
        will celar all the figures
        """
        return


    def active_extent(self):
        """
        will return the active offsets and p0 of the active window
        """
        ydelta = self.ax.viewLim.height
        print ydelta
        xdelta = self.ax.viewLim.width
        print xdelta
        offsets = self.ax.viewLim._get_p0()
        print offsets
        
        #self.activeScan 



class IVTracker:

    def __init__(self, mainUI):
        self.mainUI = mainUI
        self.transport_sweeps = []
        self.transport_names = []
        self.tran_index_value = 0
    
    def add_iv(self, iv, name = None):
        self.transport_sweeps.append(iv)
        self.transport_names.append(str(name))
        self.mainUI.TransportcomboBox.addItem(str(name))
        self.set_active_iv()

    def set_active_iv(self, value = None):
        #value set to none so it excepts a value from call back but doesn't need it to do anything
        #uses the current index anyways
        self.tran_index_value = self.mainUI.TransportcomboBox.currentIndex()
        self.transport = self.transport_sweeps[self.tran_index_value]

    def plot_active_IV(self):
        self.mainUI.mpl_2.canvas.ax.clear()
        self.mainUI.mpl_2.canvas.ax.errorbar(self.transport.sentVoltage, self.transport.dataI,  yerr = self.transport.dataIstd)
        self.mainUI.mpl_2.canvas.draw()

    def export_active_IV(self):
        #print 'export'
        temp = self.transport
        data = [temp.dataI, temp.sentVoltage, temp.dataIstd] 
        export = Exporter()
        header = export.make_header(self.transport)
        name = '../data/' + self.transport_names[self.tran_index_value]
        export.export_csv(name = name, header = header, data = data)


class ToolTracker:
    """
    
    Object for tracking behavior of tool status and setting well defined behavior



    """




    #sigHideRequested = QtCore.Signal(object)
    #sigShowRequested = QtCore.Signal(object)

    def __init__(self, mainUI):
        self.mainUI = mainUI

        self.lineState = False
        self.rectROIState = False
        self.roiCrossState = False
        self.selState = True
        self.visState = True
        self.ClickState = None 
        self.firstClick = 1
        self.secondClick = 2
        self.firstClickEvt = None
        self.secondClickEvt = None
        self.viewXhair = False

    def set_Line(self):
        if self.mainUI.Line.isChecked() == True :
            self.lineState = True
            self.rectROIState = False
            self.roiCrossState = False
            self.selState = False
            self.visState = True
            self.update_State()
        else:
            self.lineState = False

    def set_Rect(self):
        if self.mainUI.ROI.isChecked() == True:
            self.lineState = False
            self.rectROIState = True
            self.roiCrossState = False
            self.selState = False
            self.visState = True
            self.update_State()
        else:
            self.rectROIState = False


    def set_roiCross(self):
        if self.mainUI.ROICross.isChecked() == True:
            self.lineState = False
            self.rectROIState = False
            self.roiCrossState = True
            self.selState = False
            self.visState = True
            self.update_State()
        else:
            self.roiCrossState = False            


    def set_Sel(self, state = None):
        """
        This should be specifically set after events
        """
        #self.selState = state
        if self.mainUI.Sel.isChecked() == True:
            self.lineState = False
            self.rectROIState = False
            self.roiCrossState = False
            self.selState = True
            self.visState = True
            self.update_State()

            #clear click state    
            #self.ClickState = None
            #self.firstClickPos = None
            #self.secondClickPos = None
        else:
            self.selState = False            


    def set_Vis(self):
        self.visState = self.mainUI.Vis.isChecked()
        #if self.visState == False:
        #    self.hide()
        #elif self.visState == True:
        #    self.show()

    def update_State(self):
        self.mainUI.Line.setChecked(self.lineState)
        self.mainUI.ROI.setChecked(self.rectROIState)
        self.mainUI.ROICross.setChecked(self.roiCrossState)
        self.mainUI.Sel.setChecked(self.selState)
        self.mainUI.Vis.setChecked(self.visState)
 
    def set_ClickState(self, evt):
        """
        For keeping track of click state of tools

        """
        if self.ClickState == None:
            self.ClickState = 1
            self.firstClickEvt = evt
        elif self.ClickState == self.firstClick:
            self.secondClickEvt = evt 
            self.ClickState = 2
        #elif self.ClickState == self.secondClick:
            #self.ClickState = None
            #default back to Sel
            #TODO: emit signal that something happened
            self.mainUI.Sel.setChecked(True)
        #print self.ClickState

    def clearClick(self):
            self.ClickState = None
            self.firstClickEvt = None
            self.secondClickEvt = None

    def setXhair(self):
        if self.mainUI.CrossHair.isChecked() :
            self.viewXhair = True
            #self.Xhair.show()
        else :
            self.viewXhair = False
            
        


class ViewTracker:
    single = True
    quad = False

    def __init__(self, mainUI):
        """
        This seems a little to compilcated but it works... making a different widget box in QT and using auto exclusive could work but this is ok for now

        """
        self.mainUI = mainUI

    def set_Single(self):
        self.single = self.mainUI.singleView.isChecked()
        if self.single == True:
            self.quad = False
            self.mainUI.quadView.setChecked(False)
        else :
            self.mainUI.quadView.setChecked(True)

    def set_Quad(self):
        self.quad = self.mainUI.quadView.isChecked()
        if self.quad == True:
            self.single = False
            self.mainUI.singleView.setChecked(False)
        else:
            self.mainUI.singleView.setChecked(True)


        





