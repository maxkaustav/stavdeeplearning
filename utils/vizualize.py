import matplotlib.pyplot as plt
from Ipython import display as dsp

class Active_plot:
  def __init__(self,xlabel="",ylabel="",title="",scale=None):
    self.xlabel=xlabel
    self.ylabel=ylabel
    self.sec=1
    self.scale=scale
    self.tic=time.time()
    plt.title=title

  def plot(self,data):
    if time.time()-self.tic>self.sec:
      plt.cla()

      if self.scale is None:
        plt.plot(data)
      elif self.scale == 'semilogx':
        plt.semilogx(data)
      elif self.scale == 'semilogy':
        plt.semilogy(data)
      elif self.scale == 'loglog':
        plt.loglog(data)

      plt.title(self.title)
      plt.xlabel(self.xlabel)
      plt.ylabel(self.ylabel)
      dsp.clear_output(wait=True)
      dsp.display(plt.gcf())

      self.tic=time.time()
