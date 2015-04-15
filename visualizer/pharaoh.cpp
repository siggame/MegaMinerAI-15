#include "pharaoh.h"
#include "pharaohAnimatable.h"
#include "frame.h"
#include "version.h"
#include "animations.h"
#include <utility>
#include <time.h>
#include <list>
#include <iostream>

namespace visualizer
{
  Pharaoh::Pharaoh()
  {
    m_game = 0;
    m_suicide=false;
  } // Pharaoh::Pharaoh()

  Pharaoh::~Pharaoh()
  {
    destroy();
  }

  void Pharaoh::destroy()
  {
    m_suicide=true;
    wait();
    animationEngine->registerGame(0, 0);

    clear();
    delete m_game;
    m_game = 0;
    
    // Clear your memory here
    
    programs.clear();

  } // Pharaoh::~Pharaoh()

  void Pharaoh::preDraw()
  {
    const Input& input = gui->getInput();
    
    // Handle player input here
  }

  void Pharaoh::postDraw()
  {
    if( renderer->fboSupport() )
    {
#if 0
      renderer->useShader( programs["post"] ); 
      renderer->swapFBO();
      renderer->useShader( 0 );
#endif

    }
  }


  PluginInfo Pharaoh::getPluginInfo()
  {
    PluginInfo i;
    i.searchLength = 1000;
    i.gamelogRegexPattern = "Pharaoh";
    i.returnFilename = false;
    i.spectateMode = false;
    i.pluginName = "MegaMinerAI: Pharaoh Plugin";


    return i;
  } // PluginInfo Pharaoh::getPluginInfo()

  void Pharaoh::setup()
  {
    gui->checkForUpdate( "Pharaoh", "./plugins/pharaoh/checkList.md5", VERSION_FILE );
    options->loadOptionFile( "./plugins/pharaoh/pharaoh.xml", "pharaoh" );
    resourceManager->loadResourceFile( "./plugins/pharaoh/resources.r" );
  }
  
  // Give the Debug Info widget the selected object IDs in the Gamelog
  list<int> Pharaoh::getSelectedUnits()
  {
    // TODO Selection logic
    return list<int>();  // return the empty list
  }

  void Pharaoh::loadGamelog( std::string gamelog )
  {
    if(isRunning())
    {
      m_suicide = true;
      wait();
    }
    m_suicide = false;

    // BEGIN: Initial Setup
    setup();

    delete m_game;
    m_game = new parser::Game;

    if( !parser::parseGameFromString( *m_game, gamelog.c_str() ) )
    {
      delete m_game;
      m_game = 0;
      WARNING(
          "Cannot load gamelog, %s", 
          gamelog.c_str()
          );
    }
    // END: Initial Setup

    int width = getWidth();
    int height = getHeight();

    renderer->setCamera( 0, 0, width, height );
    renderer->setGridDimensions( width, height );
 
    start();
  } // Pharaoh::loadGamelog()
  
  // The "main" function
  void Pharaoh::run()
  {
    timeManager->setNumTurns( 0 );
    animationEngine->registerGame(0, 0);

    Frame * turn = new Frame;
    Frame * nextTurn = new Frame;

    int mapWidth = getWidth();
    int mapHeight = getHeight();

    Color whiteColor = Color(1, 1, 1, 1);
    parser::Tile lastTileAt [mapWidth][mapHeight];
    const string trapTypeTexture[] = {
      "trap_sarcophagus",
      "trap_snake-pit",
      "trap_swinging-blade",
      "trap_boulder",
      "trap_spider-web",
      "trap_quicksand",
      "trap_oil-vases",
      "trap_arrow-wall",
      "trap_head-wire",
      "trap_mercury-pit",
      "trap_mummy",
      "trap_fake-rotating-wall"
    };

    const string thiefTypeTexture[] = {
      "thief_bomber",
      "thief_digger",
      "thief_ninja",
      "thief_guide",
      "thief_slave"
    };

    // Look through each turn in the gamelog
    for(int state = 0; state < (int)m_game->states.size() && !m_suicide; state++)
    {
      // Parse Tiles \\
      //for(auto iter : m_game->states[state].tiles)
      for(auto& iter : m_game->states[state].tiles)
      {
        const parser::Tile& tile = iter.second;
        const int tileId = iter.first;
        lastTileAt[tile.x][tile.y] = tile;
      }

      for(int x = 0; x < mapWidth; x++)
      {
        for(int y = 0; y < mapHeight; y++)
        {
          const parser::Tile& tile = lastTileAt[x][y];
          string tileTextureKey = "tile_open";

          if(tile.type == 1)
          {
            tileTextureKey = "tile_spawn";
          }
          else if(tile.type == 2)
          {
            tileTextureKey = "tile_wall";
          }

          SmartPointer<Animatable> anim;
          SmartPointer<DrawSpriteData> spriteData = new DrawSpriteData(tile.x, tile.y, 1, 1, tileTextureKey, false);
          spriteData->addKeyFrame( new DrawSprite( spriteData, whiteColor, whiteColor ) );
          anim = spriteData;

          turn->addAnimatable( anim );
        }
      }


      //-- Parse Traps --\\
      count << "hello"
      for(auto& iter : m_game->states[state].traps)
      {
        const parser::Trap& trap = iter.second;
        const int trapId = iter.first;

        SmartPointer<Animatable> anim;
        SmartPointer<DrawSpriteData> spriteData = new DrawSpriteData(trap.x, trap.y, 1, 1, trapTypeTexture[trap.trapType], false);
        spriteData->addKeyFrame( new DrawSprite( spriteData, whiteColor, whiteColor ) );
        anim = spriteData;

        turn->addAnimatable( anim );
      }



      //-- Parse Thieves --\\
      cout < "why am I needed?";
      for(auto& iter : m_game->states[state].thiefs) // lol "thiefs"
      {
        const parser::Thief& thief = iter.second;
        const int thiefId = iter.first;

        SmartPointer<Animatable> anim;
        SmartPointer<DrawSpriteData> spriteData = new DrawSpriteData(thief.x, thief.y, 1, 1, thiefTypeTexture[thief.thiefType], false);
        spriteData->addKeyFrame( new DrawSprite( spriteData, whiteColor, whiteColor ) );
        anim = spriteData;

        turn->addAnimatable( anim );
      }



      animationEngine->buildAnimations(*turn);
      addFrame(*turn);

      // Register the game and begin playing delayed due to multithreading
      if(state > 5)
      {
        timeManager->setNumTurns(state - 5);
        animationEngine->registerGame( this, this );
        if(state == 6)
        {
          animationEngine->registerGame(this, this);
          timeManager->setTurn(0);
          timeManager->play();
        }
      }

      delete turn;
      turn = nextTurn;
      nextTurn = new Frame;
    }
    
    if(!m_suicide)
    {
      timeManager->setNumTurns( m_game->states.size() );
      timeManager->play();
    }

  } // Pharaoh::run()

} // visualizer

Q_EXPORT_PLUGIN2( Pharaoh, visualizer::Pharaoh );
